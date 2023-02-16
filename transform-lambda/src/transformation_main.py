# import packages
import zipfile
import boto3
import json
import pandas as pd
# python logging module
import logging
# import util functions
from util_functions import create_simulation_buckets

# create clients
s3 = boto3.client('s3')
lambda_client = boto3.client('lambda')
iam_client = boto3.client('iam')

'''
JOBS
.Finish s3 policy, needs debugging and attach to IAM role. 
.Once the role is complete the aws action to create lambda can be used; just assign the role in the keyword arg of lambda_client.create_function()
.REFACTOR? start moving this 'script' of aws actions into the lambda?
.create an event (trigger) that triggers lambda when csv file lands in ingestion s3 bucket. 
'''

# Simulate Ingestion Bucket
bucket_one = 'sqhellsangels-ingestion-bucket'
create_simulation_buckets()

'''CREATE ALL AWS RESOURCES + EXTRACTION, TRANSFORMATION AND LOADING OF FILES'''
# Get CSV file from ingestion bucket save locally
response = s3.get_object(Bucket=bucket_one, Key='test.csv')
with open('retrieved.csv', 'wb') as f:
    f.write(response['Body'].read())


# read CSV file into a Pandas DataFrame
df = pd.read_csv('retrieved.csv')
# convert DataFrame to Parquet format and save to file
df.to_parquet('transformed-data.parquet')


# create S3 bucket for processed data
bucket_two = 'sqhellsangels-processed-bucket'
s3.create_bucket(Bucket=bucket_two)


# Upload object to bucket
with open('transformed-data.parquet', 'rb') as f:
    s3.put_object(Bucket=bucket_two, Key='transformed-data.parquet', Body=f)


# List the objects in 'processed' s3 bucket
obj_list = s3.list_objects_v2(Bucket=bucket_two)
# print(obj_list['Contents'])


# create S3 bucket for lambda handler
bucket_three = 'sqhellsangels-lambda-bucket'
s3.create_bucket(Bucket=bucket_three)


# Create a new zip file
with zipfile.ZipFile('lambda-deployment.zip', 'w') as zip:
    # Add files to the zip file
    zip.write('lambda-handler.py')

# Add ZIP to s3 bucket
s3.upload_file('./lambda-deployment.zip',
               bucket_three, 'lambda-deployment.zip')

# List the objects in 'lambda bucket' s3 bucket
lambda_list = s3.list_objects_v2(Bucket=bucket_three)
print(lambda_list['Contents'])


'''CREATE ALL ROLES AND POLICIES'''

# CREATIAM POLICY DOCUMENT
iam_policy_doc = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
               "sts:AssumeRole"
            ],
            "Principal": {
                "Service": [
                    "lambda.amazonaws.com"
                ]
            }
        }
    ]
}

# Convert the policy from JSON dict to string
string_iam_policy = json.dumps(iam_policy_doc)

# CREATE IAM EXECUTION ROLE
# iam_response = iam_client.create_role(
#    RoleName='trans-iam-role',
#    AssumeRolePolicyDocument=string_iam_policy,
#    Tags=[
#        {
#            'Key': 'iam-role-tag',
#            'Value': ''
#        },
#    ]
# )


iam_role = iam_client.get_role(RoleName='trans-iam-role')
# iam_role_arn = iam_response['Role']['Arn']
# print(iam_role_arn)


# CREATE S3 ACCESS POLICY

# Create a bucket policy
bucket_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Principal": {"AWS": "arn:aws:iam::271939554930:role/trans-iam-role"},
            "Action": ["s3:GetObject"],
            "Resource": f"arn:aws:s3:::{bucket_one}",

        }
    ]
}

# Convert the policy from JSON dict to string
bucket_policy = json.dumps(bucket_policy)

# Set the new policy
# s3.put_bucket_policy(Bucket=bucket_one, Policy=bucket_policy)


'''DEPLOY THE LAMDA FROM THE ZIP FILE THAT IS IN THE LAMBDA S3 ON AWS'''
# THE ROLE IS COMPLETED, ONCE THE POLICY IS ATTACHED YOU CAN USE THE ROLE ARN TO CREATE THE LAMBDA on AWS. IT WILL NEED TO BE COMMONTED OUT THOUGH WHILST THE POLICY IS BEING DE-BUGGED
# Ended day on following error:
# ClientError: An error occurred (MalformedPolicy) when calling the PutBucketPolicy operation: Action does not apply to any resource(s) in statement
response = lambda_client.create_function(
    FunctionName='transformation-lambda',
    Handler='lambda-hander.lambda_handler',
    Runtime='python3.9',
    Role=iam_role['Role']['Arn'],
    Code={
        'S3Bucket': bucket_three,
        'S3Key': 'lambda-deployment.zip'
    }
)

print(response['FunctionArn'])
