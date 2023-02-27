from datetime import datetime

from timestamp import create_timestamp, retrieve_timestamp
from get_updated_data import get_updated_data
from convert_to_csv import convert_to_csv

def lambda_handler(event, context):
    latest_timestamp = retrieve_timestamp()
    
    timestamp = create_timestamp()    

    # latest_timestamp = '2020-01-01 08:00:13.016000'
    
    # x = datetime.now()
    # timestamp = x.strftime("%Y-%m-%d %H:%M")
    
    sql_data = get_updated_data(latest_timestamp)
    convert_to_csv(sql_data, timestamp)


#old lambda_handler
# def lambda_handler(event, context):
#     # timestamp = create_timestamp()    
#     # latest_timestamp = retrieve_timestamp()

#     latest_timestamp = '2023-02-23 08:00:13.016000'
#     # timestamp = '2020-02-01 08:00:13.016000'
    
#     sql_data = get_updated_data(latest_timestamp)
#     convert_to_csv(sql_data)