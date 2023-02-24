import boto3
import logging
from botocore.exceptions import ClientError
import pg8000.native as pg

logger = logging.getLogger('SQHellsLogger')
logger.setLevel(logging.INFO)

"""" example of use in  lambdas """
# utility to retrive hostname and password by db-name
def retrieve_db_secrets(db_name='warehouse'):
    sm = boto3.client('secretsmanager')
    hostname = None
    password = None
    try:
        secret_id = db_name + '_host'
        secret = sm.get_secret_value(SecretId=secret_id)
        hostname = secret['SecretString']
        secret_id = db_name + '_pswd'
        secret = sm.get_secret_value(SecretId=secret_id)
        password = secret['SecretString']

    except ClientError as e:
        logger.error("The requested secret was not found")
    return hostname, password



def connect():
    """ small utility to test the connection to warehouse database"""
    
    try:
        hostname, pswd = retrieve_db_secrets(db_name='warehouse')

        conn = pg.Connection(user='project_team_1',host=hostname,password=pswd,database='postgres')
        # simple query to check that connection is working 
        # result =conn.run('SELECT * FROM dim_currency')
        # titles = [ meta_data['name'] for meta_data in conn.columns]
        # print(f'titles: {titles}')
    except Exception as ex:
        print(f'error_msg: {ex}')
    return conn 