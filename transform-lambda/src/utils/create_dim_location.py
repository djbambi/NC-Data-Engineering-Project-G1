import boto3
import pandas as pd

# create clients
s3 = boto3.client('s3')

'''This function creates a dim location table - Key is the name the CSV in the S3 bucket to be transformed to parquet. Bucket is the S3 ingestion bucket the CSV file is taken from. bucket_two is the S3 processes bucket the parquet file is uploaded to'''
def create_dim_location(key, bucket, bucket_two):
    # Get address CSV file from the ingestion bucket
    response = s3.get_object(Bucket=bucket, Key=key)
    # Read address CSV file
    df = pd.read_csv(response['Body'])

    # change the column name in place
    df.rename(columns={'address_id': 'location_id'}, inplace=True)
    # drop the olast_updated column
    df = df.drop(columns=['last_updated'])
    # drop the created_at column
    df = df.drop(columns=['created_at'])

    transformed_dim_location = df.to_parquet()

    # Add parquet file to the processed data bucket
    s3.put_object(Bucket=bucket_two,
                  Key="dim_location.parquet",
                  Body=transformed_dim_location)