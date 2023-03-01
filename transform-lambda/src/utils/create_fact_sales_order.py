import boto3
import pandas as pd

# create clients
s3 = boto3.client('s3')

'''This function creates a fact sales order table - Key is the name the CSV in the S3 bucket to be transformed to parquet. Bucket is the S3 ingestion bucket the CSV file is taken from. bucket_two is the S3 processes bucket the parquet file is uploaded to'''
def create_fact_sales_order(key, bucket, bucket_two):
    # Get sales_order CSV file from the ingestion bucket
    response = s3.get_object(Bucket=bucket, Key=key)
    # Read sales_order CSV file
    df = pd.read_csv(response['Body'])
    # convert timestamp column to datetime format
    df['created_at'] = pd.to_datetime(df['created_at'])
    # split the timestamp column into date and time columns
    df['created_date'] = df['created_at'].dt.date
    df['created_time'] = df['created_at'].dt.time
    # drop the original timestamp column
    df = df.drop(columns=['created_at'])
    # convert timestamp column to datetime format
    df['last_updated'] = pd.to_datetime(df['last_updated'])
    # split the timestamp column into date and time columns
    df['last_updated_date'] = df['last_updated'].dt.date
    df['last_updated_time'] = df['last_updated'].dt.time
    # drop the original timestamp column
    df = df.drop(columns=['last_updated'])
    # change the column name in place
    df.rename(columns={'staff_id': 'sales_staff_id'}, inplace=True)

    # convert DataFrame to Parquet format and save to file
    transformed_sales_order = df.to_parquet()

    # Add parquet file to the processed data bucket
    s3.put_object(Bucket=bucket_two,
                  Key="dim_sales_order.parquet",
                  Body=transformed_sales_order)