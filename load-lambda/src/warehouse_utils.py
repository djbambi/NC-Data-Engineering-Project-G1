import pg8000.native as pg
from pg8000.exceptions import InterfaceError
import boto3

test_bucket = 'sqhells-transform-data'

def connect():
    try:
        hostname='nc-data-eng-project-dw-prod.chpsczt8h1nu.eu-west-2.rds.amazonaws.com'
        parole='5v8FmZSgQEdCxtN'
        conn = pg.Connection(user='project_team_1',host=hostname,password=parole,database='postgres')
        result =conn.run('SELECT * FROM dim_currency')
        titles = [ meta_data['name'] for meta_data in conn.columns]
        print(f'titles: {titles}')
    except Exception as ex:
        print(f'error_msg: {ex}')

    pass 

def list_bucket_objects(bucket_name):
    client = boto3.client('s3')
    bucket_contents = client.list_objects(Bucket=bucket_name)
    objects = []
    if 'Contents' in bucket_contents:
        objects = [obj['Key'] for obj in bucket_contents['Contents']]
    return objects

def get_bucket_objects(bucket_name):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    objects = [obj.key for obj in bucket.objects.all()]
    return objects

print(list_bucket_objects(test_bucket))
print(get_bucket_objects(test_bucket))

#connect()