import pandas as pd
from dotenv import load_dotenv
import  os
import sqlalchemy as sa
from sqlalchemy import text
import psycopg2
import seaborn as sns
import matplotlib.pyplot as plt


def connect():
    load_dotenv()

    warehouse_creds = {
        "host": os.environ.get('WAREHOUSE_HOST'), 
        "user":'project_team_1', 
        "password": os.environ.get('WAREHOUSE_PSWD'),
        "database": 'postgres'}

    wrh_url = sa.URL.create(
        "postgresql+psycopg2",
        username=warehouse_creds['user'],
        password=warehouse_creds['password'],
        host=warehouse_creds['host'],
        database=warehouse_creds['database']
    )
    wrh_engine = sa.create_engine(wrh_url).connect()
    return wrh_engine

conn = connect()

def load_dw_table(conn, table_name=''):
    df = None
    if len(table_name) > 1:
        query = text(f'SELECT * FROM {table_name} LIMIT 20')
        df = pd.read_sql_query(query,conn)
        print(df.head(5))
    return df
#load_dw_table (conn, table_name='dim_design')

def plot_sales_by_time(dw_conn, category='year'):
    # query = text(f'SELECT SUM(units_sold*unit_price) AS total, dim_date.year, dim_date.month_name FROM fact_sales_order \
    #              JOIN dim_date  ON fact_sales_order.created_date = dim_date.date_id \
    #              GROUP BY dim_date.year, dim_date.month_name ORDER BY dim_date.date_id ASC')

    query = text(f'SELECT sales_record_id, dim_date.year, dim_date.month_name as month, dim_date.day, (units_sold*unit_price) as sub_total FROM fact_sales_order \
                 JOIN dim_date  ON fact_sales_order.created_date = dim_date.date_id ORDER BY dim_date.date_id ASC')
    df_fact = pd.read_sql_query(query,dw_conn)
    print(df_fact.head(5))

    #fig,(ax1,ax2) = plt.subplots(1,2,figsize =(12,5))
    fig = plt.figure(figsize =(12,7))
    ax1 = fig.add_subplot(212)
    ax2 = fig.add_subplot(221)
    ax3 = fig.add_subplot(222)

    sns.boxplot(data=df_fact,x='year',y='sub_total',ax=ax3)
    sns.boxplot(data=df_fact,x='month',y='sub_total',ax=ax2)
    sns.boxplot(data=df_fact,x='day',y='sub_total',ax=ax1)
    ax3.set_xlabel('Year')
    ax3.set_ylabel('Sales value')
    ax3.set_title ("Year-wise Trend ")

    ax2.set_xlabel('Month')
    ax2.set_ylabel('Sales value')
    ax2.set_title('Month-wise Box Plot (Seasonality)')

    ax1.set_xlabel('Day')
    ax1.set_ylabel('Sales value')
    ax1.set_title ("Day-wise Trend ")

    fig.savefig('./results/sales_time_trends.svg',format = 'svg')
    plt.show()
    return len(df_fact)
plot_sales_by_time(conn,category='day')
