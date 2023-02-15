import boto3
# create client
s3 = boto3.client('s3')

'''In order for us to implement the correct functionalities of the "transformation function / stage" we needed to replicate some aws resources and do some initial setup; create the S3 bucket, insert a CSV file. In order for us to then be able to retrieve it and begin a transformation to parquet etc. 14/02/23'''

bucket_name = 'sqhells-angels-bucket'
# Create bucket
s3.create_bucket(Bucket=bucket_name)

# Upload object to bucket
with open('../test.csv', 'rb') as f:
    s3.put_object(Bucket=bucket_name, Key='test.csv', Body=f)

# List the files
obj_list = s3.list_objects_v2(Bucket=bucket_name)


response = s3.get_object(Bucket=bucket_name, Key='test.csv')
print(response['Body'])

with open('retrieved.txt', 'wb') as f:
    f.write(response['Body'].read())


"Setting up a lambda function to recieve s3 put object event (triggered when a file is added to the bucket)"

def lambda_handler(event, context):

    Args:
        event:
            a valid S3 PutObject event -
            see https://docs.aws.amazon.com/AmazonS3/latest/userguide/notification-content-structure.html
        context:
            a valid AWS lambda Python context object - see
            https://docs.aws.amazon.com/lambda/latest/dg/python-context.html

            https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-get-started.html
            