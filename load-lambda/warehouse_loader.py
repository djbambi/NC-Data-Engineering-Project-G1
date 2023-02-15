# import pandas as pd
import pg8000.native as pg
import boto3

def lambda_handler(event, context):
    """ Connects to the warehouse database
    On receipt of scheduled event, 
    checks for changes in the S3 bucket and loads 
    the content stored files into warehouse database
    Args:
        event:
            a valid EventBridge event -
            see https://docs.aws.amazon.com/AmazonS3/latest/userguide/notification-content-structure.html
        context:
            a valid AWS lambda Python context object - see
            https://docs.aws.amazon.com/lambda/latest/dg/python-context.html
    """
    hostname='nc-data-eng-project-dw-prod.chpsczt8h1nu.eu-west-2.rds.amazonaws.com'
    parole='5v8FmZSgQEdCxtN'
    conn = pg.Connection(user='project_team_1',host=hostname,password=parole,database='postgres')
    result =conn.run('SELECT * FROM dim_currency')
    titles = [ meta_data['name'] for meta_data in conn.columns]
    print(titles)
    return None

lambda_handler(None, None)


