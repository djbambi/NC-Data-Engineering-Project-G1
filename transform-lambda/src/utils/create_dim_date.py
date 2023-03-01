import boto3
import pandas as pd

# create clients
s3 = boto3.client('s3')

'''This function creates a dim date table - Key is the name the CSV in the S3 bucket to be transformed to parquet. Bucket is the S3 ingestion bucket the CSV file is taken from. bucket_two is the S3 processes bucket the parquet file is uploaded to'''
def create_dim_date(key, bucket, bucket_two):

    # Get sales_order CSV file from the ingestion bucket
    response = s3.get_object(Bucket=bucket, Key=key)
    # Read sales_order CSV file
    df = pd.read_csv(response['Body'])

    df['created_at'] = pd.to_datetime(df['created_at'])
    df['created_at'] = df['created_at'].dt.date
    df['last_updated'] = pd.to_datetime(df['last_updated'])
    df['last_updated'] = df['last_updated'].dt.date

    df = df.drop(columns=['sales_order_id',
                          'design_id',
                          'staff_id',
                          'counterparty_id',
                          'units_sold',
                          'unit_price',
                          'currency_id',
                          'agreed_delivery_location_id'
                          ])

    df = pd.melt(df)

    # DROP DUPLICATE ROWS
    df.drop_duplicates(subset='value', inplace=True)

    df.rename(columns={'value': 'date_id'}, inplace=True)

    df = df.drop(columns=['variable'])

    # ADD EXTRA COLUMNS
    df['date_id'] = pd.to_datetime(df['date_id'])
    df['year'] = df['date_id'].dt.year
    df['month'] = df['date_id'].dt.month
    df['day'] = df['date_id'].dt.day
    df['day_of_week'] = df['date_id'].dt.dayofweek
    df['day_name'] = df['date_id'].dt.day_name()
    df['month_name'] = df['date_id'].dt.month_name()
    df['quarter'] = df['date_id'].dt.quarter

    transformed_dim_date = df.to_parquet()

    # Add parquet file to the processed data bucket
    s3.put_object(Bucket=bucket_two,
                  Key="dim_date.parquet",
                  Body=transformed_dim_date)