import pg8000.native as pg

# Totesys connection variables:
host = 'nc-data-eng-totesys-production.chpsczt8h1nu.eu-west-2.rds.amazonaws.com'
port = 5432
database = 'totesys'
user = 'project_user_1'
password = 'Zwec2EPvgedMGtT9ATGQFnDz'

## API Connection
con = pg.Connection(user, host = host, database ='totesys', password=password)


## This function converts the Database tables to big list that consists of dictionaries, each dictionry has a key of the table name and the a value of table data in a list 
def ingest():
    tables_names = con.run("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")

    table_data = []   

    for table in tables_names:
        tables_rows = con.run(f"SELECT * FROM {table[0]};")
        table_data.append({table[0]: tables_rows})

    return table_data   
