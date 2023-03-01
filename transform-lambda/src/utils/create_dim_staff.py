import boto3
import pandas as pd

# create clients
s3 = boto3.client('s3')

'''This function creates a dim staff table - Key is the name the CSV in the S3 bucket to be transformed to parquet. Bucket is the S3 ingestion bucket the CSV file is taken from. bucket_two is the S3 processes bucket the parquet file is uploaded to'''
def create_dim_staff(key, bucket, bucket_two):
    # Get staff CSV file from the ingestion bucket
    staff_response = s3.get_object(Bucket=bucket, Key=key)
    # Read staff CSV file
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

    # Add parquet file to the processed data bucket
    s3.put_object(Bucket=bucket_two,
                  Key="dim_staff.parquet",
                  Body=transformed_dim_staff)