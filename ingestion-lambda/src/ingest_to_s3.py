import boto3
from src.bucket_names import ingestion_bucket

client = boto3.client('s3')

# Function to upload a csv file to s3, file will be stored in the /tmp folder on the lambda, and uploaded from there, should be called in a loop for each csv file, puts the files in a folder containing the date and the time which should be created when the lambda is first run, time should not end in /
def ingest_to_s3(table_name, folder_path):

    bucket = ingestion_bucket
    file_path = f'/tmp/{table_name}.csv'
    file_name = f'{folder_path}/{table_name}.csv'
        
    client.upload_file(file_path, bucket, file_name) 