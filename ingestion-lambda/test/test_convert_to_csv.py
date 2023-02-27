from src.convert_to_csv import convert_to_csv
from test_data.mock_ingested_data_function_output import *
import os
import shutil
import csv

dirname = os.path.dirname(__file__)
file_path = f"{dirname}/../src/csv_files"

def reset_folder():
    if os.path.exists(file_path):
        shutil.rmtree(file_path)
    os.mkdir(file_path)

def test_writes_a_csv_file():
    reset_folder()
        
    convert_to_csv(mock_data)

    assert os.path.exists(f"{file_path}/payment.csv") == True


def test_writes_csv_files_():
    reset_folder()

    convert_to_csv(mock_data)

    assert os.path.exists(f"{file_path}/payment.csv") == True
    assert os.path.exists(f"{file_path}/transaction.csv") == True
    assert os.path.exists(f"{file_path}/sales_order.csv") == True


def test_doesnt_save_empty_files():
    reset_folder()

    convert_to_csv(mock_data)

    assert os.path.exists(f"{file_path}/design.csv") == False
    assert os.path.exists(f"{file_path}/staff.csv") == False


def test_column_names_exist():
    reset_folder()

    convert_to_csv(mock_data2)

    with open(f"{file_path}/payment.csv", "r") as file:
        reader = csv.reader(file)
        row1 = next(reader)
        assert "payment_id" in row1
        assert "last_updated" in row1

def test_column_names_exist():
    reset_folder()
    convert_to_csv(mock_data3)

    with open("src/csv_files/payment.csv", "r") as file:
        reader = csv.reader(file)
        row1 = next(reader)
        assert "payment_id" in row1
        assert "last_updated" in row1