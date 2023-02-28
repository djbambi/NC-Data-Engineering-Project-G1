import boto3
import pandas as pd
import ccy

# create clients
s3 = boto3.client('s3')


def create_fact_sales_order(key, bucket, bucket_two):
    # GET OBJECT
    response = s3.get_object(Bucket=bucket, Key=key)
    # READ OBJECT
    df = pd.read_csv(response['Body'])
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

    s3.put_object(Bucket=bucket_two,
                  Key="dim_sales_order.parquet",
                  Body=transformed_sales_order)


def create_dim_location(key, bucket, bucket_two):
    # GET OBJECT
    response = s3.get_object(Bucket=bucket, Key=key)
    # READ OBJECT
    df = pd.read_csv(response['Body'])

    # change the column name in place
    df.rename(columns={'address_id': 'location_id'}, inplace=True)
    # drop the olast_updated column
    df = df.drop(columns=['last_updated'])
    # drop the created_at column
    df = df.drop(columns=['created_at'])

    transformed_dim_location = df.to_parquet()

    s3.put_object(Bucket=bucket_two,
                  Key="dim_location.parquet",
                  Body=transformed_dim_location)


def create_dim_design(key, bucket, bucket_two):

    # GET OBJECT
    response = s3.get_object(Bucket=bucket, Key=key)
    # READ OBJECT
    df = pd.read_csv(response['Body'])
    # drop the olast_updated column
    df = df.drop(columns=['last_updated'])
    # drop the created_at column
    df = df.drop(columns=['created_at'])

    transformed_dim_design = df.to_parquet()

    s3.put_object(Bucket=bucket_two,
                  Key="dim_design.parquet",
                  Body=transformed_dim_design)


def create_dim_currency(key, bucket, bucket_two):
    # GET OBJECT
    response = s3.get_object(Bucket=bucket, Key=key)
    # READ OBJECT
    df = pd.read_csv(response['Body'])

    # drop the olast_updated column
    df = df.drop(columns=['last_updated'])
    # drop the created_at column
    df = df.drop(columns=['created_at'])

    # use the ccy library to create a new column 'currency_name'
    df['currency_name'] = df['currency_code'].apply(
        lambda x: ccy.currency(x).name)

    transformed_dim_currency = df.to_parquet()

    s3.put_object(Bucket=bucket_two,
                  Key="dim_currency.parquet",
                  Body=transformed_dim_currency)


def create_dim_counterparty(key, bucket, bucket_two):
    # GET OBJECT
    counterparty_response = s3.get_object(Bucket=bucket, Key=key)
    # READ OBJECT
    counterparty_df = pd.read_csv(counterparty_response['Body'])

    # GET ADDRESS
    address_response = s3.get_object(Bucket=bucket, Key="address/full_address_table.csv.csv")
    # READ ADDRESS
    address_df = pd.read_csv(address_response['Body'])

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

    s3.put_object(Bucket=bucket_two,
                  Key="dim_counterparty.parquet",
                  Body=transformed_dim_counter_party)


def create_dim_staff(key, bucket, bucket_two):
    # GET STAFF
    staff_response = s3.get_object(Bucket=bucket, Key=key)
    # READ STAFF
    staff_df = pd.read_csv(staff_response['Body'])

    # GET DEPARTMENTS
    departments_response = s3.get_object(
        Bucket=bucket, Key="department/full_department_table.csv")
    # READ DEPARTMENTS
    departments_df = pd.read_csv(departments_response['Body'])

    df = staff_df.merge(departments_df[['department_id', 'department_name', 'location']],
                        left_on='department_id', right_on='department_id', how='left')

    df = df.drop(columns=['created_at', 'last_updated', 'department_id'])
    df['department_name'] = df['department_name'].fillna(value="No department")
    df['location'] = df['location'].fillna(value="No location")

    transformed_dim_staff = df.to_parquet()

    s3.put_object(Bucket=bucket_two,
                  Key="dim_staff.parquet",
                  Body=transformed_dim_staff)


def create_dim_date(key, bucket, bucket_two):

    # GET OBJECT
    response = s3.get_object(Bucket=bucket, Key=key)
    # READ OBJECT
    df = pd.read_csv(response['Body'])

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

    s3.put_object(Bucket=bucket_two,
                  Key="dim_date.parquet",
                  Body=transformed_dim_date)

def find_bucket_by_keyword(keyword='processed'):
    bucket_name = None
    client = boto3.client('s3')
    bucket_list = client.list_buckets()['Buckets']
    for bucket in bucket_list:
        if keyword in bucket['Name']:
            bucket_name = bucket['Name']
    return bucket_name