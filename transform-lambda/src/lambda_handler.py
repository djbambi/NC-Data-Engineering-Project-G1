import boto3
import pandas as pd
import utility_functions

# create clients
s3 = boto3.client('s3')


def lambda_handler(event, context):
    # Get CSV file from ingestion bucket
    bucket_one = "ingestion-bucket-hell-900"
    bucket_two = "processed-bucket-hell-900"

    time_stamp_file = s3.get_object(
        Bucket=bucket_one, Key="timestamp.txt")

    time_stamp = time_stamp_file['Body'].read().decode('utf-8').strip()

    # ALL CSV FILES IN INGESTION
    bucket_list = s3.list_objects(Bucket=bucket_one)

    for item in bucket_list['Contents']:

        key = item['Key']

        if key == f"{time_stamp}/sales_order.csv":
            utility_functions.create_fact_sales_order(
                key, bucket_one, bucket_two)
            utility_functions.create_dim_date(key, bucket_one, bucket_two)
        elif key == f"{time_stamp}/design.csv":
            utility_functions.create_dim_design(key, bucket_one, bucket_two)
        elif key == f"{time_stamp}/currency.csv":
            utility_functions.create_dim_currency(key, bucket_one, bucket_two)
        elif key == f"{time_stamp}/staff.csv":
            utility_functions.create_dim_staff(key, bucket_one, bucket_two)
        elif key == f"{time_stamp}/counterparty.csv":
            utility_functions.create_dim_counterparty(
                key, bucket_one, bucket_two)
        elif key == f"{time_stamp}/address.csv":
            utility_functions.create_dim_location(key, bucket_one, bucket_two)
