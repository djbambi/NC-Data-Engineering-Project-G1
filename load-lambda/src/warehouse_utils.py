import pg8000.native as pg
import pandas as pd
from pg8000.exceptions import InterfaceError, DatabaseError
import boto3
import logging
import io

test_bucket = 'sqhells-transform-*'
logger = logging.getLogger('SQHellsLogger')
logger.setLevel(logging.INFO)

def connect():
    """ small utility to test the connection to warehouse database"""
    try:
        hostname='nc-data-eng-project-dw-prod.chpsczt8h1nu.eu-west-2.rds.amazonaws.com'
        parole='5v8FmZSgQEdCxtN'
        conn = pg.Connection(user='project_team_1',host=hostname,password=parole,database='postgres')
        # result =conn.run('SELECT * FROM dim_currency')
        # titles = [ meta_data['name'] for meta_data in conn.columns]
        # print(f'titles: {titles}')
    except Exception as ex:
        print(f'error_msg: {ex}')
    return conn 

def list_bucket_objects(bucket_name):
    """ the function reads the name of files(keys) in the S3 bukets
        using boto3 Client
        Args: bucket name
        Returns: the client and the list of filenames (s3 keys)
    """
    try:
        client = boto3.client('s3')
        bucket_contents = client.list_objects_v2(Bucket=bucket_name)
        objects = []
        if 'Contents' in bucket_contents:
            objects = [obj['Key'] for obj in bucket_contents['Contents']]
    except Exception as e:
        logger.error(e)
    return client, objects.sort()

def get_bucket_objects(bucket_name):
    try:
        #logger.info(f'getting bucket{bucket_name}')
        s3 = boto3.resource('s3')
        bucket = s3.Bucket(bucket_name)
        objects = [obj.key for obj in bucket.objects.all()]
    except Exception as e:
        logger.error(e)
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
    data_list = data_frame.iloc[row_idx].to_list()
    zip_data_list = list(zip(col_list, data_list))
    # just in case, find the first _id column, if does not exist, use 1st
    id_col_idx = 0
    i = 0
    while id_col_idx ==0 and i < len(col_list):
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

def put_data_frame_to_table(db_conn, df_name, table_name):
    """ loops through each row in the data frame provided, 
        checks if the row _id exists in the data table 
        and inserts or updates the row accordingly
    """
    logger = logging.getLogger('warehouse_loader logger')
    logger.setLevel(logging.INFO)
    error_at_previous_row = False
    format_query = f"SELECT attname, format_type(atttypid, atttypmod) AS data_type FROM pg_attribute WHERE attrelid = '{table_name}' ::regclass AND attnum >0;"

    format_list = db_conn.run(format_query)
    """ boolean array contining "does this column contains date", 
        can be passed to the make_table_query to call the TO_DATE() function where needed
        date_format_list = [ 'date' in result[1] for result in format_list]
        #print(date_format_list)
    """ 
  
    id_date_format = False
    for result in format_list:
        id_date_format = id_date_format or ( '_id' in result[0] and 'date' in result[1] )

    for row in df_name.iterrows():
        if not error_at_previous_row:
            try:                
                query = make_table_query(df_name,table_name,row[0],type="SELECT",id_type_date=id_date_format)
                result = db_conn.run(query)
                if not result:
                    query = make_table_query(df_name, table_name,row[0],type="INSERT")
                else:
                    query = make_table_query(df_name, table_name,row[0],type="UPDATE",id_type_date=id_date_format)
                result = db_conn.run(query)
            except Exception as de:
                error_at_previous_row = True
                logger.error(f'database error - {de}')
                # logger.error('database error')

    return None



conn = connect()
staff_df = pd.read_parquet('./test_data/fact_sales_order.parquet')
#print(staff_df.head(4))
# # for row in staff_df.iterrows():
# #     print(row[1].to_list()[0])
put_data_frame_to_table(conn, staff_df, 'fact_sales_order')
