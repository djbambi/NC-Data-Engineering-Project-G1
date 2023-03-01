import boto3
import pandas as pd

# create clients
s3 = boto3.client('s3')

'''This function creates a dim counterparty table - Key is the name the CSV in the S3 bucket to be transformed to parquet. Bucket is the S3 ingestion bucket the CSV file is taken from. bucket_two is the S3 processes bucket the parquet file is uploaded to'''
def create_dim_counterparty(key, bucket, bucket_two):
    # Get counterparty CSV file from the ingestion bucket
    counterparty_response = s3.get_object(Bucket=bucket, Key=key)
    # Read counterparty CSV file
    counterparty_df = pd.read_csv(counterparty_response['Body'])

    # Get address CSV file from the ingestion bucket
    address_response = s3.get_object(Bucket=bucket, Key="address/full_address_table.csv")
    # Read address CSV file
    address_df = pd.read_csv(address_response['Body'])

    df = counterparty_df.merge(address_df[[
                               'address_id',
                               'address_line_1',
                               'address_line_2',
                               'district',
                               'city',
                               'postal_code',
                               'country',
                               'phone']], left_on='legal_address_id', right_on='address_id', how='left')

    df = df.drop(columns=['legal_address_id',
                          'commercial_contact',
                          'delivery_contact',
                          'created_at',
                          'last_updated',
                          'address_id'])

    df.rename(columns={
        'address_line_1': 'counterparty_legal_address_line_1',
        'address_line_2': 'counterparty_legal_address_line_2',
        'district': 'counterparty_legal_district',
        'city': 'counterparty_legal_city',
        'postal_code': 'counterparty_legal_postal_code',
        'phone': 'counterparty_legal_phone_number',
        'country': 'counterparty_legal_country',


    }, inplace=True)

    transformed_dim_counter_party = df.to_parquet()

    # Add parquet file to the processed data bucket
    s3.put_object(Bucket=bucket_two,
                  Key="dim_counterparty.parquet",
                  Body=transformed_dim_counter_party)