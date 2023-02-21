import boto3
import datetime
from decimal import *

client = boto3.client('s3')

main_list = [{'counterparty': []}, {'currency': []}, {'department': []}, {'design': []}, {'payment': [[1450, datetime.datetime(2023, 2, 20, 8, 31, 10, 334000), datetime.datetime(2023, 2, 20, 8, 31, 10, 334000), 1450, 7, Decimal('149774.16'), 3, 1, False, '2023-02-24', 45027817, 17590048], [1451, datetime.datetime(2023, 2, 20, 8, 49, 10, 12000), datetime.datetime(2023, 2, 20, 8, 49, 10, 12000), 1451, 17, Decimal('348811.92'), 3, 3, False, '2023-02-24', 15113326, 36100933], [1452, datetime.datetime(2023, 2, 20, 9, 11, 10, 92000), datetime.datetime(2023, 2, 20, 9, 11, 10, 92000), 1452, 10, Decimal('32189.04'), 3, 3, False, '2023-02-22', 49259988, 40171620], [1453, datetime.datetime(2023, 2, 20, 9, 21, 10, 110000), datetime.datetime(2023, 2, 20, 9, 21, 10, 110000), 1453, 11, Decimal('8968.96'), 1, 1, False, '2023-02-26', 49569199, 60120426]]}]


tables_list = [{'counterparty': []}, {'currency': []}, {'department': []}, {'design': []}, {'payment': [[1450, datetime.datetime(2023, 2, 20, 8, 31, 10, 334000), datetime.datetime(2023, 2, 20, 8, 31, 10, 334000), 1450, 7, Decimal('149774.16'), 3, 1, False, '2023-02-24', 45027817, 17590048], [1451, datetime.datetime(2023, 2, 20, 8, 49, 10, 12000), datetime.datetime(2023, 2, 20, 8, 49, 10, 12000), 1451, 17, Decimal('348811.92'), 3, 3, False, '2023-02-24', 15113326, 36100933], [1452, datetime.datetime(2023, 2, 20, 9, 11, 10, 92000), datetime.datetime(2023, 2, 20, 9, 11, 10, 92000), 1452, 10, Decimal('32189.04'), 3, 3, False, '2023-02-22', 49259988, 40171620], [1453, datetime.datetime(2023, 2, 20, 9, 21, 10, 110000), datetime.datetime(2023, 2, 20, 9, 21, 10, 110000), 1453, 11, Decimal('8968.96'), 1, 1, False, '2023-02-26', 49569199, 60120426]]}, {'sales_order': [[922, datetime.datetime(2023, 2, 20, 8, 31, 10, 334000), datetime.datetime(2023, 2, 20, 8, 31, 10, 334000), 12, 20, 7, 43539, Decimal('3.44'), 3, '2023-02-24', '2023-02-24', 1], [923, datetime.datetime(2023, 2, 20, 9, 21, 10, 110000), datetime.datetime(2023, 2, 20, 9, 21, 10, 110000), 13, 7, 11, 2288, Decimal('3.92'), 1, '2023-02-24', '2023-02-26', 30], [924, datetime.datetime(2023, 2, 20, 9, 26, 10, 85000), datetime.datetime(2023, 2, 20, 9, 26, 10, 85000), 31, 10, 5, 66093, Decimal('2.02'), 2, '2023-02-23', '2023-02-25', 5], [925, datetime.datetime(2023, 2, 20, 9, 43, 10, 384000), datetime.datetime(2023, 2, 20, 9, 43, 10, 384000), 10, 5, 17, 21380, Decimal('2.72'), 3, '2023-02-21', '2023-02-22', 23], [926, datetime.datetime(2023, 2, 20, 11, 42, 10, 215000), datetime.datetime(2023, 2, 20, 11, 42, 10, 215000), 9, 2, 5, 31099, Decimal('2.47'), 2, '2023-02-20', '2023-02-25', 4]]}]

def ingest_to_s3(table_name):
    client = boto3.client('s3')
    client.upload_file(f'/tmp/{table_name}.csv', "ingestion-bucket-data-1676971688",f'new{table_name}.csv') 

