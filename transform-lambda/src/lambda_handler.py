import boto3
import pandas as pd

# create clients
s3 = boto3.client('s3')
def lambda_handler(event, context):
    # Get CSV file from ingestion bucket
    bucket_one = "ingestion-bucket-sqhell"
    key = 'test.csv'
    response = s3.get_object(Bucket=bucket_one, Key=key)
    # read CSV file into a Pandas DataFrame
    df = pd.read_csv(response['Body'])
    print(df)
    # convert DataFrame to Parquet format and save to file
    transformed_data = df.to_parquet()
    # Upload object to bucket
    bucket_two = "processed-bucket-sqhell"
    key = 'transformed-data.parquet'
    s3.put_object(Bucket=bucket_two, Key=key, Body=transformed_data)
    return 'Data transformed and uploaded to S3'
