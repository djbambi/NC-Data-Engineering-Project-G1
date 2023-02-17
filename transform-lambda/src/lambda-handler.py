import logging
import boto3
from botocore.exceptions import ClientError
import pandas as pd

# create clients
s3 = boto3.client('s3')


def lambda_handler(event, context):
    # bucket name variables
    bucket_one = 'sqhellsangels-ingestion-bucket'
    bucket_two = 'sqhellsangels-processed-bucket'

    # GET FILE
    response = s3.get_object(Bucket=bucket_one, Key='test.csv')
    with open('/tmp/retrieved.csv', 'wb') as f:
        f.write(response['Body'].read())

    # TRANSFORM FILE
    df = pd.read_csv('/tmp/retrieved.csv')
    # convert DataFrame to Parquet format and save to file
    df.to_parquet('/tmp/transformed-data.parquet')

   # response = s3.get_object(Bucket=bucket_one, Key='test.csv')
    # object_content = response['Body'].read()
   # print(object_content)

    # df = pd(object_content)
    # df.to_parquet('transformed-data.parquet')

    with open('/tmp/transformed-data.parquet', 'rb') as f:
        s3.put_object(Bucket=bucket_two,
                      Key='transformed-data.parquet', Body=f)


'''lAMBDA JOBS
.GET CSV FILE FROM INGESTION BUCKET
.READ CSV FILE, TURN INTO DATA FRAME WITH PANDAS, TRANSFORM TO PARQUET
.UPLOAD CONVERTED DATA TO TRANSFORMED S3 BUCKET
.

'''
lambda_handler(event="hello", context="hello")

# iam = boto3.client('iam', region_name='us-east-1')
# policy = '{"Version": "2012-10-17","Statement": [{ "Effect": "Allow", "Principal": {"Service": "lambda.amazonaws.com"},"Action": "sts:AssumeRole"}]}
# response = iam.create_role( RoleName=role_name, AssumeRolePolicyDocument=lambda_role_document)
# print(iam.list_roles())
