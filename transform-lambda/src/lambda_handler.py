import boto3
import pandas as pd
from utils.create_fact_sales_order import create_fact_sales_order
from utils.create_dim_location import create_dim_location
from utils.create_dim_design import create_dim_design
from utils.create_dim_currency import create_dim_currency
from utils.create_dim_counterparty import create_dim_counterparty
from utils.create_dim_staff import create_dim_staff
from utils.create_dim_date import create_dim_date
from utils.find_bucket_name import find_bucket_by_keyword

# create clients
s3 = boto3.client('s3')

'''Lambda-handler deployed to AWS - Handles the transformation of data from CSV to star-schema parquet tables, triggered when CSV files land in the ingestion S3 bucket'''
def lambda_handler(event, context):
    # Get CSV file from ingestion bucket
    bucket_one = find_bucket_by_keyword(keyword='ingestion')
    bucket_two = find_bucket_by_keyword()

    # Get timestamp from the S3 bucket - new timestamp created when then ingestion lambda runs
    time_stamp_file = s3.get_object(
        Bucket=bucket_one, Key="timestamp/latest_timestamp.txt")

    time_stamp = time_stamp_file['Body'].read().decode('utf-8').strip()

    # ALL CSV FILES IN INGESTION
    bucket_list = s3.list_objects(Bucket=bucket_one)

    # iterates over CSV files in the bucket and calls the correct utility function
    for item in bucket_list['Contents']:

        key = item['Key']

        if key == f"{time_stamp}/sales_order.csv":
            create_fact_sales_order(
                key, bucket_one, bucket_two)
            create_dim_date(key, bucket_one, bucket_two)
        elif key == f"{time_stamp}/design.csv":
            create_dim_design(key, bucket_one, bucket_two)
        elif key == f"{time_stamp}/currency.csv":
            create_dim_currency(key, bucket_one, bucket_two)
        elif key == f"{time_stamp}/staff.csv":
            create_dim_staff(key, bucket_one, bucket_two)
        elif key == f"{time_stamp}/counterparty.csv":
            create_dim_counterparty(
                key, bucket_one, bucket_two)
        elif key == f"{time_stamp}/address.csv":
            create_dim_location(key, bucket_one, bucket_two)
