import boto3
import pandas as pd
import ccy

# create clients
s3 = boto3.client('s3')

'''This function creates a dim currency table - Key is the name the CSV in the S3 bucket to be transformed to parquet. Bucket is the S3 ingestion bucket the CSV file is taken from. bucket_two is the S3 processes bucket the parquet file is uploaded to'''
def create_dim_currency(key, bucket, bucket_two):
    # Get currency CSV file from the ingestion bucket
    response = s3.get_object(Bucket=bucket, Key=key)
    # Read currency CSV file
    df = pd.read_csv(response['Body'])

    # drop the last_updated column
    df = df.drop(columns=['last_updated'])
    # drop the created_at column
    df = df.drop(columns=['created_at'])

    # use the ccy library to create a new column 'currency_name'
    df['currency_name'] = df['currency_code'].apply(
        lambda x: ccy.currency(x).name)

    transformed_dim_currency = df.to_parquet()

    # Add parquet file to the processed data bucket
    s3.put_object(Bucket=bucket_two,
                  Key="dim_currency.parquet",
                  Body=transformed_dim_currency)
