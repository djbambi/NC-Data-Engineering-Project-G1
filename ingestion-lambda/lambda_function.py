from timestamp import create_timestamp, retrieve_timestamp, upload_timestamp
from get_database_data import get_database_data
from upload_to_s3 import upload_to_s3


def lambda_handler(event, context):
    latest_timestamp = retrieve_timestamp()

    timestamp = create_timestamp()
    upload_timestamp(timestamp)

    sql_data = get_database_data(latest_timestamp)
    upload_to_s3(sql_data, timestamp)
