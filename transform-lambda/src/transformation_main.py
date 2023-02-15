# import packages
import zipfile
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


# Create a new zip file
with zipfile.ZipFile('lambda-deployment.zip', 'w') as zip:
    # Add files to the zip file
    zip.write('lambda-handler.py')

# create S3 bucket for lambda handler
bucket_three = 'sqhellsangels-lambda-bucket'
s3.create_bucket(Bucket=bucket_three)

# List the objects in 'processed' s3 bucket
lambda_list = s3.list_objects_v2(Bucket=bucket_three)
print(lambda_list['Contents'])