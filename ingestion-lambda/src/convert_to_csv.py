import csv
import os

#This function takes a list of dictionaries of table data, which will be outputted by the ingest and the get_updated_data functions. it creates a new directory and saves each table as a seperate csv file inside that folder
def convert_to_csv(tables_list):
    os.makedirs("src/csv_files")
    for table_dict in tables_list:
        for key in table_dict.keys():
            if table_dict[key]:
                writing_func(table_dict[key], key)


#Helper function for convert_to_csv: writes any list provided to a file with the provided name into a folder called csv_files
def writing_func(list, table_name):
    with open(f"src/csv_files/{table_name}.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        for row in list:
            writer.writerow(row)