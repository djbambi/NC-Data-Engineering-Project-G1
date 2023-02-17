from connection_details import con


# This function takes the latest time the ingested table was updated as an argument, then returns the date from the SQL database after that argutment (latest time ingested table was updated) it returns a list of dictionaries, each dictionry has a key of the table name and the a value of table data in a list that consisted of nested lists that represent the rows of the table  
def get_updated_data(latest_timestamp):    

    tables_names = con.run("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
    
    table_data = []   
    print(tables_names)

    for table in tables_names:        
        query = f'SELECT * FROM {table[0]} WHERE last_updated > :time;'  
        updated_rows = con.run(query, time = latest_timestamp)
        
        table_data.append({table[0]: updated_rows})
    
    return table_data

