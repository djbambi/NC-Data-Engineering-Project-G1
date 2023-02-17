import pg8000.native as pg
from pg8000.exceptions import InterfaceError
def connect():
    try:
        hostname='nc-data-eng-project-dw-prod.chpsczt8h1nu.eu-west-2.rds.amazonaws.com'
        parole='5v8FmZSgQEdCxtN'
        conn = pg.Connection(user='project_team_1',host=hostname,password=parole,database='postgres')
        result =conn.run('SELECT * FROM dim_currency')
        titles = [ meta_data['name'] for meta_data in conn.columns]
        print(f'titles: {titles}')
    except Exception as ex:
        print(f'error_msg: {ex}')

    pass 
connect()