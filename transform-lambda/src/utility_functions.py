import pandas as pd
import ccy


def create_fact_sales_order():
    df = pd.read_csv('../mock_ingestion_bucket_11_files/csv_files/sales_order.csv')
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
    df = pd.read_csv('../mock_ingestion_bucket_11_files/csv_files/currency.csv')

    # drop the olast_updated column
    df = df.drop(columns=['last_updated'])
    # drop the created_at column
    df = df.drop(columns=['created_at'])
    
    # use the ccy library to create a new column 'currency_name'
    df['currency_name'] = df['currency_code'].apply(lambda x: ccy.currency(x).name)

    transformed_dim_currency = df.to_parquet()
    return transformed_dim_currency


def create_dim_counterparty():

    counterparty_df = pd.read_csv('../mock_ingestion_bucket_11_files/csv_files/counterparty.csv')
    address_df = pd.read_csv('../mock_ingestion_bucket_11_files/csv_files/address.csv')

    df = counterparty_df.merge(counterparty_df[['legal_address_id', 'legal_address_line_1']], left_on='legal_address_id', right_on='address_id', how='left')
    print(df)

def create_dim_staff():

    staff_df = pd.read_csv('../mock_ingestion_bucket_11_files/csv_files/staff.csv')
    departments_df = pd.read_csv('../mock_ingestion_bucket_11_files/csv_files/department.csv')

    df = staff_df.merge(departments_df[['department_id', 'department_name']], left_on='department_id', right_on='department_id', how='left')
    df = df.merge(departments_df[['department_id', 'location']], left_on='department_id', right_on='department_id', how='left')
    df = df.drop(columns=['created_at', 'last_updated'])
    df['department_name'] = df['department_name'].fillna(value="No department")
    df['location'] = df['location'].fillna(value="No location")
    
    transformed_dim_staff = df.to_parquet()
    return transformed_dim_staff



create_dim_counterparty()




