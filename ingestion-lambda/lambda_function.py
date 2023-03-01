from timestamp import create_timestamp, retrieve_timestamp, upload_timestamp
from get_sql_data import get_sql_data
from upload_to_s3 import upload_to_s3


def lambda_handler(event, context):
    """Function that will be called by the lambda in AWS
    takes all functions and calls them in the correct order"""

    latest_timestamp = retrieve_timestamp()

    timestamp = create_timestamp()
    upload_timestamp(timestamp)

    sql_data = get_sql_data(latest_timestamp)
    upload_to_s3(sql_data, timestamp)
