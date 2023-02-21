import boto3
import datetime
from decimal import *

client = boto3.client('s3')

main_list = [{'counterparty': []}, {'currency': []}, {'department': []}, {'design': []}, {'payment': [[1450, datetime.datetime(2023, 2, 20, 8, 31, 10, 334000), datetime.datetime(2023, 2, 20, 8, 31, 10, 334000), 1450, 7, Decimal('149774.16'), 3, 1, False, '2023-02-24', 45027817, 17590048], [1451, datetime.datetime(2023, 2, 20, 8, 49, 10, 12000), datetime.datetime(2023, 2, 20, 8, 49, 10, 12000), 1451, 17, Decimal('348811.92'), 3, 3, False, '2023-02-24', 15113326, 36100933], [1452, datetime.datetime(2023, 2, 20, 9, 11, 10, 92000), datetime.datetime(2023, 2, 20, 9, 11, 10, 92000), 1452, 10, Decimal('32189.04'), 3, 3, False, '2023-02-22', 49259988, 40171620], [1453, datetime.datetime(2023, 2, 20, 9, 21, 10, 110000), datetime.datetime(2023, 2, 20, 9, 21, 10, 110000), 1453, 11, Decimal('8968.96'), 1, 1, False, '2023-02-26', 49569199, 60120426]]}]


def ingest_to_s3():
    paym = payment.encode('utf-8')
    client.put_object(Bucket='ingestion-bucket-data-1676971688',Key='payment.csv',Body=paym)

