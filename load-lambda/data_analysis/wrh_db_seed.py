import pg8000.native as pg
import pandas as pd
from dotenv import load_dotenv
import  os

def connect():
    load_dotenv()
    totesys_creds = {
        "host": os.environ.get('TOTESYS_HOST'), 
        "user": 'project_user_1', 
        "password": os.environ.get('TOTESYS_PSWD'),
        "database": 'totesys'}
    wrh_conn = pg.Connection('lssgav', database = 'cp_tot_wrh')
    tot_conn = pg.Connection(user= totesys_creds['user'],
        host= totesys_creds['host'],
        password= totesys_creds['password'],
        database= totesys_creds['database'])
    return tot_conn, wrh_conn
