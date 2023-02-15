import boto3
# create client
s3 = boto3.client('s3')
lambda_client = boto3.client('lambda')

'''In or'''

bucket_one = 'ingested_bucket'
# Create bucket
s3.create_bucket(Bucket=bucket_one)

# Upload object to bucket
with open('./test.csv', 'rb') as f:
    s3.put_object(Bucket=bucket_one, Key='test.csv', Body=f)

# List the files
obj_list = s3.list_objects_v2(Bucket=bucket_one)





"Setting up a lambda function to recieve s3 put object event (triggered when a file is added to the bucket)"

'''

.getobject should retrieve file, transform to parquet format and then saves it locally to a csv.
.then uploads transformed data to a 'processed data' s3 bucket.
. get lambda zipped with dependancies and put onto aws. 
.Create a new IAM role for the Lambda function with permissions to access the S3 bucket. Note down the ARN of the role.
.Define the Lambda function's configuration:

'''

def lambda_handler(event, context):
    response = s3.get_object(Bucket=bucket_one, Key='test.csv')
    print(response['Body'])

    with open('retrieved.txt', 'wb') as f:
        f.write(response['Body'].read())
    

    # Args:
    #     event:
    #         a valid S3 PutObject event -
    #         see https://docs.aws.amazon.com/AmazonS3/latest/userguide/notification-content-structure.html
    #     context:
    #         a valid AWS lambda Python context object - see
    #         https://docs.aws.amazon.com/lambda/latest/dg/python-context.html

    #         https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-get-started.html