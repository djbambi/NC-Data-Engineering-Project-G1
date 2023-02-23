import pandas as pd
import ccy
import datetime


def create_fact_sales_order():
    df = pd.read_csv(
        '../mock_ingestion_bucket_11_files/csv_files/sales_order.csv')
    # convert timestamp column to datetime format
    df['created_at'] = pd.to_datetime(df['created_at'])
    # split the timestamp column into date and time columns
    df['created_date'] = df['created_at'].dt.date
    df['created_time'] = df['created_at'].dt.time
    # drop the original timestamp column
    df = df.drop(columns=['created_at'])
    # convert timestamp column to datetime format
    df['last_updated'] = pd.to_datetime(df['last_updated'])
    # split the timestamp column into date and time columns
    df['last_updated_date'] = df['last_updated'].dt.date
    df['last_updated_time'] = df['last_updated'].dt.time
    # drop the original timestamp column
    df = df.drop(columns=['last_updated'])
    # change the column name in place
    df.rename(columns={'staff_id': 'sales_staff_id'}, inplace=True)
    # convert DataFrame to Parquet format and save to file
    transformed_sales_order = df.to_parquet()
    return transformed_sales_order


def create_dim_location():
    df = pd.read_csv('../mock_ingestion_bucket_11_files/csv_files/address.csv')
    # change the column name in place
    df.rename(columns={'address_id': 'location_id'}, inplace=True)
    # drop the olast_updated column
    df = df.drop(columns=['last_updated'])
    # drop the created_at column
    df = df.drop(columns=['created_at'])
    transformed_dim_location = df.to_parquet()
    return transformed_dim_location


def create_dim_design():
    df = pd.read_csv('../mock_ingestion_bucket_11_files/csv_files/design.csv')

    # drop the olast_updated column
    df = df.drop(columns=['last_updated'])
    # drop the created_at column
    df = df.drop(columns=['created_at'])

    transformed_dim_design = df.to_parquet()
    return transformed_dim_design


def create_dim_currency():
    df = pd.read_csv(
        '../mock_ingestion_bucket_11_files/csv_files/currency.csv')

    # drop the olast_updated column
    df = df.drop(columns=['last_updated'])
    # drop the created_at column
    df = df.drop(columns=['created_at'])

    # use the ccy library to create a new column 'currency_name'
    df['currency_name'] = df['currency_code'].apply(
        lambda x: ccy.currency(x).name)

    transformed_dim_currency = df.to_parquet()
    return transformed_dim_currency


def create_dim_counterparty():

    counterparty_df = pd.read_csv(
        '../mock_ingestion_bucket_11_files/csv_files/counterparty.csv')
    address_df = pd.read_csv(
        '../mock_ingestion_bucket_11_files/csv_files/address.csv')

    df = counterparty_df.merge(address_df[[
                               'address_id',
                               'address_line_1',
                               'address_line_2',
                               'district',
                               'city',
                               'postal_code',
                               'country',
                               'phone']], left_on='legal_address_id', right_on='address_id', how='left')

    df = df.drop(columns=['legal_address_id',
                          'commercial_contact',
                          'delivery_contact',
                          'created_at',
                          'last_updated',
                          'address_id'])

    df.rename(columns={
        'address_line_1': 'counterparty_legal_address_line_1',
        'address_line_2': 'counterparty_legal_address_line_2',
        'district': 'counterparty_legal_district',
        'city': 'counterparty_legal_city',
        'postal_code': 'counterparty_legal_postal_code',
        'phone': 'counterparty_legal_phone_number',
        'country': 'counterparty_legal_country',


    }, inplace=True)

    transformed_dim_counter_party = df.to_parquet()
    return transformed_dim_counter_party


def create_dim_staff():

    staff_df = pd.read_csv(
        '../mock_ingestion_bucket_11_files/csv_files/staff.csv')
    departments_df = pd.read_csv(
        '../mock_ingestion_bucket_11_files/csv_files/department.csv')

    df = staff_df.merge(departments_df[['department_id', 'department_name', 'location']],
                        left_on='department_id', right_on='department_id', how='left')

    df = df.drop(columns=['created_at', 'last_updated'])
    df['department_name'] = df['department_name'].fillna(value="No department")
    df['location'] = df['location'].fillna(value="No location")

    transformed_dim_staff = df.to_parquet()
    return transformed_dim_staff


def create_dim_date():

    df = pd.read_csv(
        '../mock_ingestion_bucket_11_files/csv_files/sales_order.csv')

    df['created_at'] = pd.to_datetime(df['created_at'])
    df['created_at'] = df['created_at'].dt.date
    df['last_updated'] = pd.to_datetime(df['last_updated'])
    df['last_updated'] = df['last_updated'].dt.date

    df = df.drop(columns=['sales_order_id',
                          'design_id',
                          'staff_id',
                          'counterparty_id',
                          'units_sold',
                          'unit_price',
                          'currency_id',
                          'agreed_delivery_location_id'
                          ])

    df = pd.melt(df)

    # DROP DUPLICATE ROWS
    df.drop_duplicates(subset='value', inplace=True)

    df.rename(columns={'value': 'date_id'}, inplace=True)

    df = df.drop(columns=['variable'])

    # ADD EXTRA COLUMNS
    df['date_id'] = pd.to_datetime(df['date_id'])
    df['year'] = df['date_id'].dt.year
    df['month'] = df['date_id'].dt.month
    df['day'] = df['date_id'].dt.day
    df['day_of_week'] = df['date_id'].dt.dayofweek
    df['day_name'] = df['date_id'].dt.day_name()
    df['month_name'] = df['date_id'].dt.month_name()
    df['quarter'] = df['date_id'].dt.quarter

    transformed_dim_date = df.to_parquet()
    return transformed_dim_date
