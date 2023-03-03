from timestamp import create_timestamp, retrieve_timestamp, upload_timestamp
from get_sql_data import get_sql_data
from upload_to_s3 import upload_to_s3
from get_bucket_name import find_bucket_by_keyword
import logging

logger = logging.getLogger('SQHellsIngestionLogger')
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    """ Function that will be called by the lambda in AWS
    takes all functions and calls them in the correct order """

    ingestion_bucket = find_bucket_by_keyword("ingestion")

    latest_timestamp = retrieve_timestamp(ingestion_bucket)

    timestamp = create_timestamp()
    upload_timestamp(timestamp, ingestion_bucket)

    sql_data = get_sql_data(latest_timestamp)

    upload_files = upload_to_s3(sql_data, timestamp, ingestion_bucket)

    logger.info(f"Successfully uploaded {upload_files} to {ingestion_bucket}")
