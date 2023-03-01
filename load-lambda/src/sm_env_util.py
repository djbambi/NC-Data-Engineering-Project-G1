import os
import boto3
from botocore.exceptions import ClientError
import pg8000.native as pg
from dotenv import load_dotenv

def load_db_creds():
    """ Reads the database hostnamse and passwords from .env file
        using dotenv module and than
        uses AWS Secret Manager and boto3 to save credentials as secret
        credentials can thne be retrieved using SecredId of
        'totesys_host', 'totesys_pswd', 'warehouse_host', 'warehouse_pswd'
    """
    load_dotenv()
    warehouse_check = False
    totesys_check = False
    sm = boto3.client('secretsmanager')
    warehouse_creds = {
        "host": os.environ.get('WAREHOUSE_HOST'), 
        "user":'project_team_1', 
        "password": os.environ.get('WAREHOUSE_PSWD'),
        "database": 'postgres'}
    totesys_creds = {
        "host": os.environ.get('TOTESYS_HOST'), 
        "user": 'project_user_1', 
        "password": os.environ.get('TOTESYS_PSWD'),
        "database": 'totesys'}
    warehouse_check = warehouse_creds['host'] != None and warehouse_creds['password'] != None
    totesys_check = totesys_creds['host'] != None and totesys_creds['password'] != None
    if totesys_check:
        secret_id = 'totesys_host'
        secret_str = totesys_creds['host']
        try:
            sm.create_secret(Name=secret_id, SecretString=secret_str)
            print('totesys secret 1 saved ')
        except ClientError as e:
            raise e
        secret_id = 'totesys_pswd'
        secret_str = totesys_creds['password']
        try:
            sm.create_secret(Name=secret_id, SecretString=secret_str)
            print('totesys secret 2 saved ')
        except ClientError as e:
            raise e
    else:
        totesys_creds = None
    if warehouse_check:
        secret_id = 'warehouse_host'
        secret_str = warehouse_creds['host']
        try:
            sm.create_secret(Name=secret_id, SecretString=secret_str)
            print('warehouse secret 1 saved ')
        except ClientError as e:
            raise e
        secret_id = 'warehouse_pswd'
        secret_str = warehouse_creds['password']
        try:
            sm.create_secret(Name=secret_id, SecretString=secret_str)
            print('warehouse secret 2 saved ')
        except ClientError as e:
            raise e
    else:
        warehouse_creds = None
    
    return totesys_creds, warehouse_creds



print(load_db_creds())
