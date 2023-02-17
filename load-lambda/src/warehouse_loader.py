import pandas as pd
import pg8000.native as pg
import boto3
import logging
from botocore.exceptions import ClientError

logger = logging.getLogger('MyLogger')
logger.setLevel(logging.INFO)

#this will be put into secrets manager later
hostname='nc-data-eng-project-dw-prod.chpsczt8h1nu.eu-west-2.rds.amazonaws.com'
parole='5v8FmZSgQEdCxtN'

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
        s3_bucket_name, s3_object_name, warehouse_conn = get_warehouse_connection(event,hostname,parole)
        logger.info(f'Bucket is {s3_bucket_name}')
        logger.info(f'Object key is {s3_object_name}')

    except ClientError as c:
        if c.response['Error']['Code'] == 'NoSuchKey':
            logger.error(f'No object found - {s3_object_name}')
        elif c.response['Error']['Code'] == 'NoSuchBucket':
            logger.error(f'No such bucket - {s3_bucket_name}')
    
    return None


def get_object_path(records):
    """Extracts bucket and object references from Records field of event."""
    return records[0]['s3']['bucket']['name'], \
        records[0]['s3']['object']['key']


def get_warehouse_connection(event, host_name, pswd):
    """Connects to the warehouse database
        extracts the bucket and the object from the event records,
        raises exceptions if s3 or postgress errors occur and logs them 
        Args: event: a valid EventBridge event 
        Returns: a tuple of Bucket name, object name and connection"""
    try:
        s3_bucket_name, s3_object_name = get_object_path(event['Records'])
        logger.info(f'Bucket is {s3_bucket_name}')
        logger.info(f'Object key is {s3_object_name}')
    except ClientError as c:
        if c.response['Error']['Code'] == 'NoSuchKey':
            logger.error(f'No object found - {s3_object_name}')
        elif c.response['Error']['Code'] == 'NoSuchBucket':
            logger.error(f'No such bucket - {s3_bucket_name}')
    try: 
        conn = pg.Connection(user='project_team_1',host=host_name,password=pswd,database='postgres')
        # result =conn.run('SELECT * FROM dim_currency')
        # titles = [ meta_data['name'] for meta_data in conn.columns]
        # logger.info(f'titles: {titles}')
    except Exception as ex:
        logger.error(f'connection error: {ex}')
    return s3_bucket_name, s3_object_name, conn

