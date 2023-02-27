import json
import boto3
from bucket_names import ingestion_bucket
import re

client = boto3.client("s3")


"""This function takes a list of dictionaries of table data, which will be outputted by the ingest and the get_updated_data functions. it creates a new directory and saves each table as a seperate csv file inside that folder"""
def convert_to_csv(tables_list, timestamp):
    for table_dict in tables_list:
        for key in table_dict.keys():
            if table_dict[key]:
                upload_to_s3(table_dict[key], key, timestamp)


"""Helper function to take each table, convert it to a string, and write it to the correct path and file name in the s3 ingestion bucket"""
def upload_to_s3(table_rows_list, table_name, timestamp):

    bucket_key = f"{timestamp}/{table_name}.csv"
    if "full" in table_name:
        name_search = re.search("full_(.*)_table", table_name)
        extracted_name = name_search.group(1)
        bucket_key = f"{extracted_name}/{table_name}.csv"

    csv_list = []

    for row in table_rows_list:
        my_array = []

        for element in row:
            my_array.append(json.dumps(element, default=str).strip('"'))

        csv_list.append(",".join(my_array))

    csv_string = "\n".join(csv_list)

    client.put_object(Body=csv_string, Bucket=ingestion_bucket, Key=bucket_key)
