import pg8000.native as pg
import pandas as pd
from pg8000.exceptions import InterfaceError, DatabaseError
import boto3
import logging
import io
from datetime import datetime as dt
from dotenv import load_dotenv
import os

logger = logging.getLogger('SQHellsLogger')
logger.setLevel(logging.INFO)



def list_bucket_objects(bucket_name, latest_only=False, time_tolerance=200):
    """ the function reads the name of files(keys) in the S3 bukets
        using boto3 Client
        Args:   bucket name
                latest_only - whether to return the key(s) modified latest
        Returns: the client and the list of filenames (s3 keys),
       
    """
    file_names = []
    objects = []
    try:
        client = boto3.client('s3')
        bucket_contents = client.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in bucket_contents:
            objects = [{"name": obj['Key'],"datetime":obj['LastModified']} for obj in bucket_contents['Contents']]
            objects.sort(key= lambda item: item['datetime'], reverse= True)
            file_times = [obj['LastModified'] for obj in bucket_contents['Contents']]
            file_times.sort(reverse= True)
            if latest_only:
                for obj in objects:
                    delta = file_times[0]-obj['datetime']
                    if delta.total_seconds() < time_tolerance:
                        print(delta.total_seconds())
                        file_names.append(obj['name'])
            else :
                file_names = [obj['name'] for obj in objects]
            file_names.sort()
    except Exception as e:
        logger.error(e)
    return client, file_names

def get_bucket_objects(bucket_name):
    try:
        #logger.info(f'getting bucket{bucket_name}')
        s3 = boto3.resource('s3')
        bucket = s3.Bucket(bucket_name)
        objects = [obj.key for obj in bucket.objects.all()]
    except Exception as e:
        logger.error(e)
    objects.sort()
    return objects


def get_data_from_file(client, bucket, object_key):
    """Reads the text from specified file in S3, used for AWS lambda testing."""
    #logger.info(f'object key is {object_key}')
    try:
        data = client.get_object(Bucket=bucket, Key=object_key)
        df = pd.read_parquet(io.BytesIO(data['Body'].read()), engine="pyarrow")
    except Exception as e:
        logger.error(e)
    return df



def extract_table_name(file_key):
    """ extracts the name  warehouse database table
    from the file name in S3 bucket, acting on presumption that
    .parqet file names corresponds to the star schema: dim_* or fact_* """
    base_idx = file_key.rfind('/')
    ext_idx = file_key.rfind('.')
    return file_key[base_idx+1 : ext_idx]

def make_table_query(data_frame, table_name, row_idx, type="INSERT", id_type_date=False):
    """ goes through the dataframe column names and prepares the SQL query
    to INSERT or UPDATE the specified row in 
    the specified table using the data from dataframe """
    query_str = ""
    col_list = data_frame.columns.to_list()
    if 'fact' in table_name:
        logger.info(f"colums: {col_list}")
    data_list = data_frame.iloc[row_idx].to_list()
    zip_data_list = list(zip(col_list, data_list))
    # just in case, find the first _id column, if does not exist, use 1st
    id_col_idx = -1
    i = 0
    while id_col_idx < 0 and i < len(col_list):
        if '_id' in col_list[i]:
            id_col_idx = i
        i += 1
    
    if type == "INSERT":
        query_str += f"INSERT INTO {table_name} ("
        val_str = ""
        for col_name in col_list:
            val_str += col_name + ", "
        query_str += val_str.rstrip(", ") + ") VALUES ("
        val_str = ""
        for value in data_list:
            val_str += f"'{value}', "
        query_str += val_str.rstrip(", ") + ");"

    
    elif type == "UPDATE":
        query_str += f"UPDATE {table_name} SET "
        val_str = ''
        for val in zip_data_list:
            val_str += f"{val[0]}='{val[1]}', "
        query_str += val_str.rstrip(", ") + " WHERE "
        if id_type_date:
            query_str += f"{col_list[id_col_idx]}=TO_DATE('{data_list[id_col_idx]}','YYYY-MM-DD');"
        else:
            query_str += f"{col_list[id_col_idx]}={data_list[id_col_idx]};"

    else :
        query_str += f"SELECT * FROM {table_name} WHERE "
        if id_type_date:
            query_str += f"{col_list[id_col_idx]}=TO_DATE('{data_list[id_col_idx]}','YYYY-MM-DD');"
        else:
            query_str += f"{col_list[id_col_idx]}={data_list[id_col_idx]};"

    return query_str
def create_dim_date_table(db_conn):
    start_date_str = '2021-01-01'
    num_days = 2000
    insert_query = """ 
    INSERT INTO dim_date
    SELECT
        ts_seq AS date_id,
        extract(year FROM ts_seq) AS year,
        CAST(extract (month FROM ts_seq) AS INTEGER) AS month,
        extract(day FROM ts_seq) AS day,
        extract(isodow FROM ts_seq) AS day_of_week,
        to_char(ts_seq, 'TMDay') AS day_name,
        TO_CHAR(ts_seq, 'TMMonth') AS month_name,
        extract(quarter FROM ts_seq) AS quarter
    FROM """
    check_query = "select COUNT(date_id) from dim_date where year > 2020;"
    result = db_conn.run(check_query)
    if result[0][0] > 0 :
        td = dt.today()
        start_date_str = td.today().isoformat()
        num_days = 72
        check_query = f"select * from dim_date where date_id=TO_DATE('{start_date_str}','YYYY-MM-DD');"
        result = db_conn.run(check_query)
        if len(result) > 0:
            return "dim_date table is up-to-date"

    insert_query += f" (SELECT '{start_date_str}' :: DATE + sequence.day AS ts_seq FROM GENERATE_SERIES(0, {num_days}) AS sequence(day)) dq; "
    result = db_conn.run(insert_query)
    check_query = "select COUNT(date_id) from dim_date  where year > 2020;"
    result = db_conn.run(check_query)
    return str(result)

def put_data_frame_to_table(db_conn, df_name, table_name):
    """ loops through each row in the data frame provided, 
        checks if the row _id exists in the data table 
        and inserts or updates the row accordingly
    """
    logger = logging.getLogger('warehouse_loader logger')
    logger.setLevel(logging.INFO)
    error_at_previous_row = False
    inserted_rows = 0
    updates_rows = 0
    format_query = f"SELECT attname, format_type(atttypid, atttypmod) AS data_type FROM pg_attribute WHERE attrelid = '{table_name}' ::regclass AND attnum >0;"
    try:
        format_list = db_conn.run(format_query)
        """ boolean array contining "does this column contains date", 
            can be passed to the make_table_query to call the TO_DATE() function where needed
            date_format_list = [ 'date' in result[1] for result in format_list]
            #print(date_format_list)
        """ 
        # if 'fact' in table_name:
        #     alter_query = "ALTER TABLE {table_name} DISABLE TRIGGER ALL;"
        #     #when done alter_query = "ALTER TABLE {table_name} ENABLE TRIGGER ALL;"
            
        if 'date' in table_name:
                logger.info(create_dim_date_table(db_conn))
        else:
            id_date_format = False
            for result in format_list:
                id_date_format = id_date_format or ( '_id' in result[0] and 'date' in result[1] )

            for row in df_name.iterrows():
                if not error_at_previous_row:
                    query = make_table_query(df_name,table_name,row[0],type="SELECT",id_type_date=id_date_format)
                    result = db_conn.run(query)
                    if not result:
                        query = make_table_query(df_name, table_name,row[0],type="INSERT")
                        inserted_rows += 1
                    else:
                        query = make_table_query(df_name, table_name,row[0],type="UPDATE",id_type_date=id_date_format)
                        updates_rows += 1
                    result = db_conn.run(query)

    except Exception as de:
        error_at_previous_row = True
        logger.error(f'database error - {de}')
    return inserted_rows, updates_rows


""" This utility finds the S3 bucket for ingested or processed data
    using the agreed keys for  the bucket name prefix
    Args: keyword
"""

def find_bucket_by_keyword(keyword='processed'):
    bucket_name = None
    client = boto3.client('s3')
    bucket_list = client.list_buckets()['Buckets']
    for bucket in bucket_list:
        if keyword in bucket['Name']:
            bucket_name = bucket['Name']
    return bucket_name

