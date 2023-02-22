import boto3
import pandas as pd

# create clients
s3 = boto3.client('s3')


def lambda_handler(event, context):
    # Get CSV file from ingestion bucket
    bucket_one = "ingestion-bucket-hell-6"
    bucket_list = s3.list_objects(Bucket=bucket_one)
    for item in bucket_list['Contents']:
        key = item['Key']
        # Get CSV file from ingestion bucket
        response = s3.get_object(Bucket=bucket_one, Key=key)
        # read CSV file into a Pandas DataFrame
        df = pd.read_csv(response['Body'])
        # convert DataFrame to Parquet format and save to file
        transformed_data = df.to_parquet()
        # Upload object to bucket
        bucket_two = "processed-bucket-hell-6"
        key = f'transformed-{key[:-4]}.parquet'
        s3.put_object(Bucket=bucket_two, Key=key, Body=transformed_data)
    return 'Data transformed and uploaded to S3'
