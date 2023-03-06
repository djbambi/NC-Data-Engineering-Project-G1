import pg8000.native as pg
import boto3

sm = boto3.client('secretsmanager')

database = 'totesys'
user = 'project_user_1'


def retrieve_db_secrets(db_name=database):
    """ This function retrieves the hostname and password
    required for the connection to the database
    which have been stored in AWS secrets manager """

    hostname = None
    password = None

    try:
        secret_id = db_name + '_host'
        secret = sm.get_secret_value(SecretId=secret_id)
        hostname = secret['SecretString']

        secret_id = db_name + '_pswd'
        secret = sm.get_secret_value(SecretId=secret_id)
        password = secret['SecretString']

    except Exception:
        raise ConnectionError("Could not find host and password secrets.")

    return hostname, password


def warehouse_connection():
    """ This function creates a connection to the totesys database,
    and returns it to be used in other modules """

    host, password = retrieve_db_secrets()

    return pg.Connection(user, host=host, database=database, password=password)
