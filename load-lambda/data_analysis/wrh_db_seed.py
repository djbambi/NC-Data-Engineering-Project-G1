import pg8000.native as pg
import pandas as pd
from dotenv import load_dotenv
import  os
import sqlalchemy as sa
import psycopg2


def connect():
    load_dotenv()
    totesys_creds = {
        "host": os.environ.get('TOTESYS_HOST'), 
        "user": 'project_user_1', 
        "password": os.environ.get('TOTESYS_PSWD'),
        "database": 'totesys'}
    warehouse_creds = {
        "host": os.environ.get('WAREHOUSE_HOST'), 
        "user":'project_team_1', 
        "password": os.environ.get('WAREHOUSE_PSWD'),
        "database": 'postgres'}

    tot_url = sa.URL.create(
        "postgresql+psycopg2",
        username="project_user_1",
        password=totesys_creds['password'],
        host=totesys_creds['host'],
        database="totesys"
    )
    wrh_url = sa.URL.create(
        "postgresql+psycopg2",
        username=warehouse_creds['user'],
        password=warehouse_creds['password'],
        host=warehouse_creds['host'],
        database=warehouse_creds['database']
    )
    tot_engine = sa.create_engine(tot_url).connect()
    wrh_engine = sa.create_engine(wrh_url).connect()
    #wrh_engine = sa.create_engine("postgresql+psycopg2://lssgav@localhost/cp_tot_wrh").connect()
    return tot_engine, wrh_engine
    # return tot_conn, wrh_conn

def load_dw_table(conn, table_name=''):
    df = None
    if len(table_name) > 1:
        file_path = f'./data_csv/{table_name}.csv'
        df = pd.read_sql(table_name, conn)
        print(df.head(5))
        df.to_csv(file_path)
    return df

tot_conn, wrh_conn = connect()

# load_dw_table(wrh_conn,'dim_date')
# load_dw_table(wrh_conn,'dim_design')
# load_dw_table(wrh_conn,'dim_counterparty')
# load_dw_table(wrh_conn,'dim_currency')
# load_dw_table(wrh_conn,'dim_location')
# load_dw_table(wrh_conn,'fact_sales_order')


# def seed_dim_staff():
#     staff_df = pd.read_sql('staff',tot_conn)
#     departments_df = pd.read_sql('department', tot_conn)
#     df = staff_df.merge(departments_df[['department_id', 'department_name', 'location']],
#                         left_on='department_id', right_on='department_id', how='left')

#     dim_staff_df = df.drop(columns=['created_at', 'last_updated','department_id'])
#     dim_staff_df['department_name'] = df['department_name'].fillna(value="No department")
#     dim_staff_df['location'] = df['location'].fillna(value="No location")
#     print(dim_staff_df.head(10))
#     result = dim_staff_df.to_sql('dim_staff', wrh_conn, index=False,if_exists='replace')
#     return result

