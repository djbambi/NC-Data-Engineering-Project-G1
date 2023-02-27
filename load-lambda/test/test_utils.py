from src.warehouse_utils import (
            extract_table_name, 
            make_table_query, 
            put_data_frame_to_table,
            list_bucket_objects)
import pandas as pd
from unittest.mock import Mock, patch
import pg8000.native as pg
from pg8000.exceptions import DatabaseError as DatabaseErr
import logging
from datetime import datetime
import boto3

def test_extracts_from_simple_path():
    test_path_1 = 'dim_date.csv'
    test_path_2 = 'dim_date.parquet'
    assert extract_table_name(test_path_1) == 'dim_date'
    assert extract_table_name(test_path_2) == 'dim_date'

def test_extracts_from_complex_path():
    test_path_1 = 'folder/2023-21-21/dim_date.csv'
    test_path_2 = 'folder/2023-21-21/dim_date.parquet'
    assert extract_table_name(test_path_1) == 'dim_date'
    assert extract_table_name(test_path_2) == 'dim_date'



def test_makes_query_to_insert_dim_staff():
    staff_df = pd.read_csv('./test_data/CSVs/dim_staff.csv')
    # print(staff_df.head(3))
    # print(staff_df.iloc[1].to_list())
    test_query_str = "INSERT INTO dim_staff (staff_id, first_name, last_name, department_name, location, email_address) VALUES ('2', 'AAA2', 'BBBBBBB2', 'test_dept_2', '2', 'test1@email.co2');"
    assert make_table_query(staff_df, 'dim_staff', 1) == test_query_str

def test_makes_query_to_insert_fact_sales():
    sales_df = pd.read_csv('./test_data/CSVs/fact_sales_order.csv')
    test_query_str = "INSERT INTO fact_sales_order (sales_record_id, sales_order_id, created_date, created_time, last_updated_date, last_updated_time, sales_staff_id, counterparty_id, units_sold, unit_price, currency_id, design_id, agreed_payment_date, agreed_delivery_date, agreed_delivery_location_id) VALUES ('3', '4', '2021-01-03', '03:01:01', '2021-01-03', '03:01:01', '2', '4', '12', '120', '2', '3', '2021-01-13', '2021-01-12', '3');"
    assert make_table_query(sales_df, 'fact_sales_order', 2) == test_query_str

def test_makes_query_to_update_dim_staff():
    staff_df = pd.read_csv('./test_data/CSVs/dim_staff.csv')
    # print(staff_df.head(3))
    # print(staff_df.iloc[1].to_list())
    test_query_str = "UPDATE dim_staff SET staff_id='2', first_name='AAA2', last_name='BBBBBBB2', department_name='test_dept_2', location='2', email_address='test1@email.co2' WHERE staff_id=2;"
    assert make_table_query(staff_df, 'dim_staff', 1, type="UPDATE") == test_query_str

def test_makes_query_to_select_from_dim_staff():
    staff_df = pd.read_csv('./test_data/CSVs/dim_staff.csv')
    test_query_str = "SELECT * FROM dim_staff WHERE staff_id=1;"
    assert make_table_query(staff_df, 'dim_staff', 0, 
    type="SELECT") == test_query_str
    test_query_str = "SELECT * FROM dim_staff WHERE staff_id=3;"
    assert make_table_query(staff_df, 'dim_staff', 2, 
    type="SELECT") == test_query_str

mock_connection=Mock()
mock_connection.run.side_effect = DatabaseErr


mock_logger=Mock()

@patch.object(pg, 'Connection', return_value=mock_connection)
@patch.object(logging, 'getLogger', return_value=mock_logger)
def test_put_datafrom_to_table_logs_error(*args):
    print(dir(mock_connection.run))
    staff_df = pd.read_csv('./test_data/CSVs/dim_staff.csv')
    put_data_frame_to_table(mock_connection, staff_df,'dim_staff')
    # mock_logger.error.assert_called_once_with('database error')
    mock_logger.error.assert_called_with('database error')

mock_s3 = Mock()

mock_response = {
    "Contents":[
         {"Key": 'file_1', "LastModified": datetime(2023, 2, 20, 12, 0, 0)},
         {"Key": 'file_4', "LastModified": datetime(2023, 2, 20, 12, 24, 30)},
         {"Key": 'file_5', "LastModified": datetime(2023, 2, 20, 12, 25, 40)},
         {"Key": 'file_2', "LastModified": datetime(2023, 2, 20, 12, 0, 50)},
         {"Key": 'file_3', "LastModified": datetime(2023, 2, 20, 12, 0, 51)}
    ],
    "Size": 123,
    "StorageClass": 'STANDARD'
}
mock_s3.list_objects_v2.return_value = mock_response
@patch.object(boto3, 'client', return_value=mock_s3)
def test_list_files_in_bucket_sorted_by_time(*args):
    client, file_list = list_bucket_objects('test_bucket')
    assert file_list == ['file_5', 'file_4', 'file_3', 'file_2', 'file_1']

@patch.object(boto3, 'client', return_value=mock_s3)
def test_list_only_recent_files_in_bucket(*args):
    client, file_list = list_bucket_objects('test_bucket', latest_only=True)
    assert file_list == ['file_5']
    client, file_list = list_bucket_objects('test_bucket', latest_only=True, time_tolerance=300)
    assert file_list == ['file_5', 'file_4']