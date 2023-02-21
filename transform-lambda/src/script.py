import zipfile
import boto3
import json
import pandas as pd

# create clients
s3 = boto3.client('s3')

# Create a new zip file
with zipfile.ZipFile('lambda-deployment.zip', 'w') as zip:
    # Add files to the zip file
    zip.write('lambda_handler.py')