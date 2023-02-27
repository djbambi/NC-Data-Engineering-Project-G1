import csv
from ingest_to_s3 import transfer_to_s3
import os
import json
import boto3
from bucket_names import ingestion_bucket
dirname = os.path.dirname(__file__)
path_to_csv_files = "csv_files"

client = boto3.client("s3")

#This function takes a list of dictionaries of table data, which will be outputted by the ingest and the get_updated_data functions. it creates a new directory and saves each table as a seperate csv file inside that folder
def convert_to_csv(tables_list, timestamp):
    for table_dict in tables_list:
        for key in table_dict.keys():
            # print(table_dict[key], key)
            if table_dict[key]:
                writing_func(table_dict[key], key, timestamp)


#Helper function for convert_to_csv: writes any list provided to a file with the provided name into a folder called csv_files, the output should go to ingest_to_S3 function to be uploaded on the Ingest S3 bucket

# def writing_func(list, table_name, timestamp):    
#     with open(f"{dirname}/{path_to_csv_files}/{table_name}.csv", "w+", encoding="utf-8") as file:
#         writer = csv.writer(file)
#         for row in list:
#             writer.writerow(row)

#     transfer_to_s3(table_name, timestamp)

def writing_func(table_rows_list, table_name, timestamp):
    csv_list = []
    for row in table_rows_list:
        my_array = []
        for element in row:
            my_array.append(json.dumps(element, default=str))
        csv_list.append(",".join(my_array))
    csv_string = "\n".join(csv_list)
    boto3.put_object(Body=csv_string, Bucket=ingestion_bucket, key=f"{timestamp}/{table_name}.csv")
    print(csv_string)
