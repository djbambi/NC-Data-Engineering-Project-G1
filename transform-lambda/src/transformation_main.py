# import packages
import boto3
import pandas as pd
# python logging module
import logging
# import util functions
from util_functions import create_simulation_buckets

# create clients
s3 = boto3.client('s3')
lambda_client = boto3.client('lambda')

'''
STEPS
.start creating and  testing lambda
. get lambda zipped with dependancies and put onto aws. 
.Create a new IAM role for the Lambda function with permissions to access the S3 bucket. Note down the ARN of the role.
.Define the Lambda function's configuration: ie 
.create an event (trigger) that triggers lambda when csv file lands in ingestion s3 bucket. 
'''

# Simulate Ingestion Bucket
bucket_one = 'sqhellsangels-ingestion-bucket'
create_simulation_buckets()

# Get CSV file from ingestion bucket save locally
response = s3.get_object(Bucket=bucket_one, Key='test.csv')


with open('retrieved.csv', 'wb') as f:
    f.write(response['Body'].read())


# read CSV file into a Pandas DataFrame
df = pd.read_csv('retrieved.csv')

# convert DataFrame to Parquet format and save to file
df.to_parquet('transformed-data.parquet')


# create S3 bucket for processed data
bucket_two = 'sqhellsangels-processed-bucket'
s3.create_bucket(Bucket=bucket_two)
# Upload object to bucket
with open('transformed-data.parquet', 'rb') as f:
    s3.put_object(Bucket=bucket_two, Key='transformed-data.parquet', Body=f)

# List the objects in 'processed' s3 bucket
obj_list = s3.list_objects_v2(Bucket=bucket_two)
print(obj_list['Contents'])


"Setting up a lambda function to recieve s3 put object event (triggered when a file is added to the bucket)"


def lambda_handler(event, context):
    pass


# Args:
#     event:
#         a valid S3 PutObject event -
#         see https://docs.aws.amazon.com/AmazonS3/latest/userguide/notification-content-structure.html
#     context:
#         a valid AWS lambda Python context object - see
#         https://docs.aws.amazon.com/lambda/latest/dg/python-context.html

#         https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-get-started.html


# iam = boto3.client('iam', region_name='us-east-1')
# policy = '{"Version": "2012-10-17","Statement": [{ "Effect": "Allow", "Principal": {"Service": "lambda.amazonaws.com"},"Action": "sts:AssumeRole"}]}
# response = iam.create_role( RoleName=role_name, AssumeRolePolicyDocument=lambda_role_document)
# print(iam.list_roles())
