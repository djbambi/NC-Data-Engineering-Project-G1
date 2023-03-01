import boto3
import pandas as pd

# create clients
s3 = boto3.client('s3')

'''This function finds the bucket name of an S3 bucket using a keyword'''
def find_bucket_by_keyword(keyword='processed'):
    bucket_name = None
    client = boto3.client('s3')
    bucket_list = client.list_buckets()['Buckets']
    for bucket in bucket_list:
        if keyword in bucket['Name']:
            bucket_name = bucket['Name']
    return bucket_name