from datetime import datetime
import boto3
from get_bucket_name import ingestion_bucket

timestamp_key = 'timestamp/latest_timestamp.txt'
client = boto3.client("s3")


def create_timestamp():
    """ Creates a timestamp of the current time
    and modifies it into the format: YYYY-MM-DD HH:MM
    (eg. 2021-02-21 13:57) """

    current_time = datetime.now()
    timestamp = current_time.strftime("%Y-%m-%d %H:%M")

    return timestamp


def upload_timestamp(timestamp):
    """ Uploads a timestamp in the format output by the
    create_timestamp function,
    in a txt file to s3 ingestion bucket """

    client.put_object(
        Body=timestamp,
        Bucket=ingestion_bucket,
        Key=timestamp_key)


def retrieve_timestamp():
    """ Retrieves latest timestamp from the
    timestamp folder in the s3 ingestion bucket.
    If not found, returns a timestamp to
    be used as an initial ingestion """

    result = client.list_objects(Bucket=ingestion_bucket, Prefix="timestamp/")

    if 'Contents' in result:
        data = client.get_object(Bucket=ingestion_bucket, Key=timestamp_key)
        latest_timestamp = data["Body"].read().decode()
        return latest_timestamp

    else:
        return "2020-01-01 00:00"
