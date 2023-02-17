# import packages
import zipfile
import boto3
import json
import pandas as pd

# create clients
s3 = boto3.client('s3')


bucket_three = 'sqhellsangels-lambda-bucket'

# Create a new zip file
with zipfile.ZipFile('lambda-deployment.zip', 'w') as zip:
    # Add files to the zip file
    zip.write('lambda-handler.py')

# Add ZIP to s3 bucket
s3.upload_file('./lambda-deployment.zip',
               bucket_three, 'lambda-deployment.zip')
