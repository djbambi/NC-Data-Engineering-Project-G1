import csv
from ingest_to_s3 import transfer_to_s3
import os

dirname = os.path.dirname(__file__)
path_to_csv_files = "csv_files"



#This function takes a list of dictionaries of table data, which will be outputted by the ingest and the get_updated_data functions. it creates a new directory and saves each table as a seperate csv file inside that folder
def convert_to_csv(tables_list, timestamp):
    for table_dict in tables_list:
        for key in table_dict.keys():
            if table_dict[key]:
                writing_func(table_dict[key], key, timestamp)


#Helper function for convert_to_csv: writes any list provided to a file with the provided name into a folder called csv_files, the output should go to ingest_to_S3 function to be uploaded on the Ingest S3 bucket

def writing_func(list, table_name, timestamp):    
    with open(f"{dirname}/{path_to_csv_files}/{table_name}.csv", "w+", encoding="utf-8") as file:
        writer = csv.writer(file)
        for row in list:
            writer.writerow(row)

    transfer_to_s3(table_name, timestamp)