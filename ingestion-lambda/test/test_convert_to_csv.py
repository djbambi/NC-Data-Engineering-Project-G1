from src.convert_to_csv import convert_to_csv
from test_data.mock_ingested_data_function_output import mock_data, mock_data2
import os
import shutil
import csv


# def test_writes_a_csv_file():
#     if os.path.exists("./src/csv_files"):
#         shutil.rmtree("src/csv_files")

#     convert_to_csv(mock_data)

#     assert os.path.exists("./src/csv_files/payment.csv") == True


# def test_writes_csv_files_():
#     if os.path.exists("./src/csv_files"):
#         shutil.rmtree("src/csv_files")

#     convert_to_csv(mock_data)

#     assert os.path.exists("./src/csv_files/payment.csv") == True
#     assert os.path.exists("./src/csv_files/transaction.csv") == True
#     assert os.path.exists("./src/csv_files/sales_order.csv") == True


# def test_doesnt_save_empty_files():
#     if os.path.exists("./src/csv_files"):
#         shutil.rmtree("src/csv_files")

#     assert os.path.exists("./src/csv_files/design.csv") == False
#     assert os.path.exists("./src/csv_files/staff.csv") == False


# def test_column_names_exist():
#     if os.path.exists("./src/csv_files"):
#         shutil.rmtree("src/csv_files")

#     convert_to_csv(mock_data2)

#     with open("./src/csv_files/payment.csv", "r") as file:
#         if os.path.exists("./src/csv_files"):
#             shutil.rmtree("src/csv_files")

#         convert_to_csv(mock_data2)

#         reader = csv.reader(file)
#         row1 = next(reader)
#         assert "payment_id" in row1
#         assert "last_updated" in row1

def test_converts_json():
    if os.path.exists("./src/csv_files"):
        shutil.rmtree("src/csv_files")
        
    convert_to_csv(mock_data2)
    assert 1 == 2