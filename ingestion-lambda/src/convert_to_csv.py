import csv
import os


def convert_to_csv(tables_list):
    os.makedirs("src/csv_files")
    for table_dict in tables_list:
        for key in table_dict.keys():
            if table_dict[key]:
                writing_func(table_dict[key], key)


def writing_func(list, table_name):
    with open(f"src/csv_files/{table_name}.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        for row in list:
            writer.writerow(row)