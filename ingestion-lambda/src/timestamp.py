from datetime import datetime
import boto3
from bucket_names import ingestion_bucket

bucket = ingestion_bucket
timestamp_key = 'timestamp/latest-timestamp.txt'
client = boto3.client("s3")


"""Creates a timestamp when the lambda is run, to be used for the next time the lambda is run to query the SQL tote database, and to save the csv files into a folder with the timestamp as its name"""
def create_timestamp():
    current_time = datetime.now()
    timestamp = current_time.strftime("%Y-%m-%d %H:%M")

    with open(f"/tmp/latest_timestamp.txt", "w+") as file:
        file.write(timestamp)
            
    client = boto3.client('s3')
    client.upload_file(f'/tmp/latest_timestamp.txt', ingestion_bucket,f'timestamp/latest_timestamp.txt')

    return timestamp
 

# """Retrives latest timestamp from the timesstamp folder in the s3 ingestion bucket"""
# def retrieve_timestamp():
#     data = client.get_object(Bucket=bucket, Key=timestamp_key)
#     contents = data['Body'].read().decode()
#     return contents


# """Uploads new timestamp to s3 ingestion bucket"""
# def upload_timestamp(timestamp):
#     client.put_object(Body=timestamp, Bucket=bucket, Key=timestamp_key)


##When Abdulrrah comes back we can refactor the top two functions instead of the this bottom one
def retrieve_timestamp():
    client = boto3.client('s3')
    
    result = client.list_objects(Bucket=ingestion_bucket, Prefix="timestamp/")
    exists=False

    if 'Contents' in result:               
        data = client.get_object(Bucket= ingestion_bucket, Key='timestamp/latest_timestamp.txt')
        latest_timestamp = data["Body"].read().decode()
        return latest_timestamp
        
    else:
        return "2020-01-01 00:00"