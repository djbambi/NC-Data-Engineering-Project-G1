from upload_to_s3 import upload_to_s3
# from test_data.mock_ingested_data_function_output import *
# from test_data.mock_convert_to_csv_function_output import *
from test_data.mock_updated_data_output import test_data
import os
import shutil
import csv

dirname = os.path.dirname(__file__)
file_path = f"{dirname}/../csv_files"


def reset_folder():
    if os.path.exists(file_path):
        shutil.rmtree(file_path)
    os.mkdir(file_path)


def test_writes_a_csv_file():
    reset_folder()

    upload_to_s3(test_data, "1")

    assert os.path.exists(f"{file_path}/payment.csv")


# def test_writes_csv_files_():
#     reset_folder()

#     convert_to_csv(mock_data)

#     assert os.path.exists(f"{file_path}/payment.csv")
#     assert os.path.exists(f"{file_path}/transaction.csv")
#     assert os.path.exists(f"{file_path}/sales_order.csv")


# def test_doesnt_save_empty_files():
#     reset_folder()

#     convert_to_csv(mock_data)

#     assert os.path.exists(f"{file_path}/design.csv") == False
#     assert os.path.exists(f"{file_path}/staff.csv") == False


# def test_column_names_exist():
#     reset_folder()

#     convert_to_csv(mock_data2)

#     with open(f"{file_path}/payment.csv", "r") as file:
#         reader = csv.reader(file)
#         row1 = next(reader)
#         assert "payment_id" in row1
#         assert "last_updated" in row1


# def test_column_names_exist():
#     reset_folder()
#     convert_to_csv(mock_data3)

#     with open("csv_files/payment.csv", "r") as file:
#         reader = csv.reader(file)
#         row1 = next(reader)
#         assert "payment_id" in row1
#         assert "last_updated" in row1


# def test_upload_to_s3_doesnt_error():
#     assert upload_to_s3(test_data2, test_name2, "2023-01-01 12:00") == 1
