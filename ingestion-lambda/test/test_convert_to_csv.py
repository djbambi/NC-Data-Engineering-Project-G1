from convert_to_csv import convert_to_csv, writing_func
from test_data.mock_ingested_data_function_output import *
import os
import shutil
import csv

dirname = os.path.dirname(__file__)
file_path = f"{dirname}/../csv_files"

def reset_folder():
    if os.path.exists(file_path):
        shutil.rmtree(file_path)
    os.mkdir(file_path)

# def test_writes_a_csv_file():
#     reset_folder()
        
#     convert_to_csv(mock_data)

#     assert os.path.exists(f"{file_path}/payment.csv") == True


# def test_writes_csv_files_():
#     reset_folder()

#     convert_to_csv(mock_data)

#     assert os.path.exists(f"{file_path}/payment.csv") == True
#     assert os.path.exists(f"{file_path}/transaction.csv") == True
#     assert os.path.exists(f"{file_path}/sales_order.csv") == True


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



test_data1 = [[1450, datetime.datetime(2023, 2, 20, 8, 31, 10, 334000), datetime.datetime(2023, 2, 20, 8, 31, 10, 334000), 1450, 7, Decimal('149774.16'), 3, 1, False, '2023-02-24', 45027817, 17590048], [1451, datetime.datetime(2023, 2, 20, 8, 49, 10, 12000), datetime.datetime(2023, 2, 20, 8, 49, 10, 12000), 1451, 17, Decimal('348811.92'), 3, 3, False, '2023-02-24', 15113326, 36100933], [1452, datetime.datetime(2023, 2, 20, 9, 11, 10, 92000), datetime.datetime(2023, 2, 20, 9, 11, 10, 92000), 1452, 10, Decimal('32189.04'), 3, 3, False, '2023-02-22', 49259988, 40171620], [1453, datetime.datetime(2023, 2, 20, 9, 21, 10, 110000), datetime.datetime(2023, 2, 20, 9, 21, 10, 110000), 1453, 11, Decimal('8968.96'), 1, 1, False, '2023-02-26', 49569199, 60120426], [1454, datetime.datetime(2023, 2, 20, 9, 26, 10, 85000), datetime.datetime(2023, 2, 20, 9, 26, 10, 85000), 1454, 5, Decimal('133507.86'), 2, 1, False, '2023-02-25', 94371097, 99760364], [1455, datetime.datetime(2023, 2, 20, 9, 43, 10, 384000), datetime.datetime(2023, 2, 20, 9, 43, 10, 384000), 1455, 17, Decimal('58153.60'), 3, 1, False, '2023-02-22', 19800822, 30055139], [1456, datetime.datetime(2023, 2, 20, 9, 51, 10, 418000), datetime.datetime(2023, 2, 20, 9, 51, 10, 418000), 1456, 9, Decimal('276680.60'), 1, 3, False, '2023-02-23', 37842933, 61880265], [1457, datetime.datetime(2023, 2, 20, 11, 30, 10, 308000), datetime.datetime(2023, 2, 20, 11, 30, 10, 308000), 1457, 10, Decimal('485797.50'), 3, 3, False, '2023-02-25', 75013896, 94000026], [1458, datetime.datetime(2023, 2, 20, 11, 42, 10, 215000), datetime.datetime(2023, 2, 20, 11, 42, 10, 215000), 1458, 5, Decimal('76814.53'), 2, 1, False, '2023-02-25', 12444713, 11652283], [1459, datetime.datetime(2023, 2, 20, 11, 47, 9, 917000), datetime.datetime(2023, 2, 20, 11, 47, 9, 917000), 1459, 16, Decimal('96965.70'), 1, 3, False, '2023-02-23', 39449220, 58313239], [1460, datetime.datetime(2023, 2, 20, 11, 52, 9, 880000), datetime.datetime(2023, 2, 20, 11, 52, 9, 880000), 1460, 18, Decimal('202983.48'), 3, 1, False, '2023-02-20', 85823754, 59406694], [1461, datetime.datetime(2023, 2, 20, 11, 52, 9, 881000), datetime.datetime(2023, 2, 20, 11, 52, 9, 881000), 1461, 13, Decimal('486896.15'), 3, 3, False, '2023-02-24', 45388222, 96727990], [1462, datetime.datetime(2023, 2, 20, 11, 57, 10, 87000), datetime.datetime(2023, 2, 20, 11, 57, 10, 87000), 1462, 19, Decimal('922611.78'), 3, 3, False, '2023-02-25', 56201703, 89865207], [1463, datetime.datetime(2023, 2, 20, 11, 57, 10, 102000), datetime.datetime(2023, 2, 20, 11, 57, 10, 102000), 1463, 10, Decimal('100961.02'), 1, 1, False, '2023-02-25', 56621848, 28912560], [1464, datetime.datetime(2023, 2, 20, 11, 58, 9, 953000), datetime.datetime(2023, 2, 20, 11, 58, 9, 953000), 1464, 9, Decimal('183069.62'), 2, 1, False, '2023-02-23', 96420863, 18594314], [1465, datetime.datetime(2023, 2, 20, 11, 59, 9, 820000), datetime.datetime(2023, 2, 20, 11, 59, 9, 820000), 1465, 15, Decimal('104701.56'), 3, 3, False, '2023-02-26', 40070765, 86262237], [1466, datetime.datetime(2023, 2, 20, 12, 2, 10, 186000), datetime.datetime(2023, 2, 20, 12, 2, 10, 186000), 1466, 14, Decimal('94138.80'), 3, 1, False, '2023-02-23', 79259339, 43409106], [1467, datetime.datetime(2023, 2, 20, 12, 11, 10, 464000), datetime.datetime(2023, 2, 20, 12, 11, 10, 464000), 1467, 8, Decimal('286962.89'), 2, 1, False, '2023-02-25', 33455296, 48415504], [1468, datetime.datetime(2023, 2, 20, 12, 15, 10, 510000), datetime.datetime(2023, 2, 20, 12, 15, 10, 510000), 1468, 12, Decimal('164151.00'), 3, 1, False, '2023-02-21', 50091708, 41516456], [1469, datetime.datetime(2023, 2, 20, 12, 37, 10, 434000), datetime.datetime(2023, 2, 20, 12, 37, 10, 434000), 1469, 1, Decimal('225873.99'), 1, 1, False, '2023-02-26', 39599301, 72207804], [1470, datetime.datetime(2023, 2, 20, 12, 44, 10, 145000), datetime.datetime(2023, 2, 20, 12, 44, 10, 145000), 1470, 16, Decimal('320835.90'), 1, 1, False, '2023-02-25', 94573156, 59333163], [1471, datetime.datetime(2023, 2, 20, 12, 51, 10, 116000), datetime.datetime(2023, 2, 20, 12, 51, 10, 116000), 1471, 5, Decimal('10945.92'), 1, 3, False, '2023-02-20', 57464545, 38297471], [1472, datetime.datetime(2023, 2, 20, 13, 10, 10, 169000), datetime.datetime(2023, 2, 20, 13, 10, 10, 169000), 1472, 12, Decimal('272514.48'), 3, 1, False, '2023-02-21', 87477393, 18916595], [1473, datetime.datetime(2023, 2, 20, 13, 25, 10, 474000), datetime.datetime(2023, 2, 20, 13, 25, 10, 474000), 1473, 6, Decimal('175807.20'), 2, 1, False, '2023-02-20', 65148393, 80292406]]
test_name1 = "payment"
test_data2 = [[1450, 'SALE', 922, None, datetime.datetime(2023, 2, 20, 8, 31, 10, 334000), datetime.datetime(2023, 2, 20, 8, 31, 10, 334000)], [1451, 'PURCHASE', None, 529, datetime.datetime(2023, 2, 20, 8, 49, 10, 12000), datetime.datetime(2023, 2, 20, 8, 49, 10, 12000)], [1452, 'PURCHASE', None, 530, datetime.datetime(2023, 2, 20, 9, 11, 10, 92000), datetime.datetime(2023, 2, 20, 9, 11, 10, 92000)], [1453, 'SALE', 923, None, datetime.datetime(2023, 2, 20, 9, 21, 10, 110000), datetime.datetime(2023, 2, 20, 9, 21, 10, 110000)], [1454, 'SALE', 924, None, datetime.datetime(2023, 2, 20, 9, 26, 10, 85000), datetime.datetime(2023, 2, 20, 9, 26, 10, 85000)], [1455, 'SALE', 925, None, datetime.datetime(2023, 2, 20, 9, 43, 10, 384000), datetime.datetime(2023, 2, 20, 9, 43, 10, 384000)], [1456, 'PURCHASE', None, 531, datetime.datetime(2023, 2, 20, 9, 51, 10, 418000), datetime.datetime(2023, 2, 20, 9, 51, 10, 418000)], [1457, 'PURCHASE', None, 532, datetime.datetime(2023, 2, 20, 11, 30, 10, 308000), datetime.datetime(2023, 2, 20, 11, 30, 10, 308000)], [1458, 'SALE', 926, None, datetime.datetime(2023, 2, 20, 11, 42, 10, 215000), datetime.datetime(2023, 2, 20, 11, 42, 10, 215000)], [1459, 'PURCHASE', None, 533, datetime.datetime(2023, 2, 20, 11, 47, 9, 917000), datetime.datetime(2023, 2, 20, 11, 47, 9, 917000)], [1460, 'SALE', 927, None, datetime.datetime(2023, 2, 20, 11, 52, 9, 880000), datetime.datetime(2023, 2, 20, 11, 52, 9, 880000)], [1461, 'PURCHASE', None, 534, datetime.datetime(2023, 2, 20, 11, 52, 9, 881000), datetime.datetime(2023, 2, 20, 11, 52, 9, 881000)], [1462, 'PURCHASE', None, 535, datetime.datetime(2023, 2, 20, 11, 57, 10, 87000), datetime.datetime(2023, 2, 20, 11, 57, 10, 87000)], [1463, 'SALE', 928, None, datetime.datetime(2023, 2, 20, 11, 57, 10, 102000), datetime.datetime(2023, 2, 20, 11, 57, 10, 102000)], [1464, 'SALE', 929, None, datetime.datetime(2023, 2, 20, 11, 58, 9, 953000), datetime.datetime(2023, 2, 20, 11, 58, 9, 953000)], [1465, 'PURCHASE', None, 536, datetime.datetime(2023, 2, 20, 11, 59, 9, 820000), datetime.datetime(2023, 2, 20, 11, 59, 9, 820000)], [1466, 'SALE', 930, None, datetime.datetime(2023, 2, 20, 12, 2, 10, 186000), datetime.datetime(2023, 2, 20, 12, 2, 10, 186000)], [1467, 'SALE', 931, None, datetime.datetime(2023, 2, 20, 12, 11, 10, 464000), datetime.datetime(2023, 2, 20, 12, 11, 10, 464000)], [1468, 'SALE', 932, None, datetime.datetime(2023, 2, 20, 12, 15, 10, 510000), datetime.datetime(2023, 2, 20, 12, 15, 10, 510000)], [1469, 'SALE', 933, None, datetime.datetime(2023, 2, 20, 12, 37, 10, 434000), datetime.datetime(2023, 2, 20, 12, 37, 10, 434000)], [1470, 'SALE', 934, None, datetime.datetime(2023, 2, 20, 12, 44, 10, 145000), datetime.datetime(2023, 2, 20, 12, 44, 10, 145000)], [1471, 'PURCHASE', None, 537, datetime.datetime(2023, 2, 20, 12, 51, 10, 116000), datetime.datetime(2023, 2, 20, 12, 51, 10, 116000)], [1472, 'SALE', 935, None, datetime.datetime(2023, 2, 20, 13, 10, 10, 169000), datetime.datetime(2023, 2, 20, 13, 10, 10, 169000)], [1473, 'SALE', 936, None, datetime.datetime(2023, 2, 20, 13, 25, 10, 474000), datetime.datetime(2023, 2, 20, 13, 25, 10, 474000)]]
test_name2 = "transaction"

def test_writing_func_outputs_correctly():
    writing_func(test_data1, test_name1)
    assert 1 == 2