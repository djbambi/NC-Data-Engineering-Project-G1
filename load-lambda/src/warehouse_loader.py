import pandas as pd
import pg8000.native as pg
import boto3
import logging
from botocore.exceptions import ClientError
from botocore.response import StreamingBody

from pg8000.exceptions import InterfaceError, DatabaseError

from warehouse_utils import logger, list_bucket_objects, get_data_from_file, extract_table_name, put_data_frame_to_table


#this will be put into secrets manager later


def lambda_handler(event, context):
    """ Connects to the warehouse database
    On receipt of scheduled event, 
    checks for changes in the S3 bucket and loads 
    the content stored files into warehouse database
    Args:
        event:
            a valid EventBridge event -
            see https://docs.aws.amazon.com/AmazonS3/latest/userguide/notification-content-structure.html
        context:
            a valid AWS lambda Python context object - see
            https://docs.aws.amazon.com/lambda/latest/dg/python-context.html
    """
    try:
        # hostname, pswd = retrieve_db_secrets(db_name='totesys')
        hostname, pswd = retrieve_db_secrets()
        s3_bucket_name, warehouse_conn = get_warehouse_connection(event,hostname,pswd)
        logger.info(f'Bucket is {s3_bucket_name}')
        s3_client, object_names = list_bucket_objects(s3_bucket_name)
        logger.info(f'Object keys are  {object_names}')
        if (len(object_names)>6):
            for object_key in object_names:
                table_name = extract_table_name(object_key)
                parquet_df = get_data_from_file(s3_client, s3_bucket_name, object_key)
                parquet_df.replace("'",'',inplace=True, regex=True)
                inserted_rows, updated_rows = put_data_frame_to_table(warehouse_conn, parquet_df, table_name)
                logger.info(f'Modifed:{table_name} inserted {inserted_rows}, updated {updated_rows} rows')

    except ClientError as c:
        if c.response['Error']['Code'] == 'NoSuchKey':
            logger.error(f'No object found - {s3_object_name}')
        elif c.response['Error']['Code'] == 'NoSuchBucket':
            logger.error(f'No such bucket - {s3_bucket_name}')
    except DatabaseError as de:
                logger.error(f'database error - {de}')
                # logger.error('database error')
    
    return None


def get_object_path(records):
    """Extracts bucket and object references from Records field of event."""
    return records[0]['s3']['bucket']['name'], records[0]['s3']['object']['key']


def get_warehouse_connection(event, host_name, pswd):
    """Connects to the warehouse database
        extracts the bucket and the object from the event records,
        raises exceptions if s3 or postgress errors occur and logs them 
        Args: event: a valid EventBridge event 
        Returns: a tuple of Bucket name, object name and connection"""
    s3_bucket_name = ''
    try:
        logger.info(f"event is {event['Records']}")
    except ClientError as c:
        if c.response['Error']['Code'] == 'NoSuchKey':
            logger.error(f'No object found ')
        elif c.response['Error']['Code'] == 'NoSuchBucket':
            logger.error(f'No such bucket - {s3_bucket_name}')
    try: 
        conn = pg.Connection(user='project_team_1',host=host_name,password=pswd,database='postgres')
        # result =conn.run('SELECT * FROM dim_currency')
        # titles = [ meta_data['name'] for meta_data in conn.columns]
        # logger.info(f'titles: {titles}')
    except Exception as ex:
        logger.error(f'connection error: {ex}')
    return s3_bucket_name, conn

def retrieve_db_secrets(db_name='warehouse'):
    sm = boto3.client('secretsmanager')
    hostname = None
    password = None
    try:
        secret_id = db_name + '_host'
        secret = sm.get_secret_value(SecretId=secret_id)
        hostname = secret['SecretString']
        secret_id = db_name + '_pswd'
        secret = sm.get_secret_value(SecretId=secret_id)
        password = secret['SecretString']

    except ClientError as e:
        logger.error("The requested secret was not found")
    return hostname, password