from datetime import datetime

from timestamp import create_timestamp, retrieve_timestamp
from get_updated_data import get_updated_data
from convert_to_csv import convert_to_csv


def lambda_handler(event, context):
    latest_timestamp = retrieve_timestamp()
    
    timestamp = create_timestamp()    
    
    sql_data = get_updated_data(latest_timestamp)
    convert_to_csv(sql_data, timestamp)
