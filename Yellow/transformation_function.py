import boto3

# create client
s3 = boto3.client('s3')

bucket_name = 'sqhells-angels-bucket'
# Create bucket
s3.create_bucket(Bucket=bucket_name)

# Upload object to bucket
with open('./test.csv', 'rb') as f:
    s3.put_object(Bucket=bucket_name, Key='test.csv', Body=f)

# List the files
obj_list=s3.list_objects_v2(Bucket=bucket_name)
print(obj_list['Contents'])
