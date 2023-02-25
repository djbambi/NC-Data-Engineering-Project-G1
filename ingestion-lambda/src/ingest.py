from src.connection_details import con

## This function converts the Database tables to big list that consists of dictionaries, each dictionry has a key of the table name and the a value of table data in a list that consisted of nested lists that represent the rows of the table  
def ingest():
    tables_names = con.run("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")  

    table_data = []   

    for table in tables_names:
        tables_rows = con.run(f"SELECT * FROM {table[0]};")
        table_data.append({table[0]: tables_rows})        

    return table_data   

