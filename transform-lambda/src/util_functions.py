import boto3
s3 = boto3.client('s3')


def create_simulation_buckets():
    bucket_one = 'sqhellsangels-ingestion-bucket'
    # Create bucket
    s3.create_bucket(Bucket=bucket_one)
    # Upload object to bucket
    with open('./test.csv', 'rb') as f:
        s3.put_object(Bucket=bucket_one, Key='test.csv', Body=f)
    # List the files
    obj_list = s3.list_objects_v2(Bucket=bucket_one)
