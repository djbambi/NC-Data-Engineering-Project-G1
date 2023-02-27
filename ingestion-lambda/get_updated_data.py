from db_connection import con

# This function takes the latest time the ingested table was updated as an argument, then returns the date from the SQL database after that argutment (latest time ingested table was updated) it returns a list of dictionaries, each dictionry has a key of the table name and the a value of table data in a list that consisted of nested lists that represent the rows of the table  
def get_updated_data(latest_timestamp):    

    tables_names = con.run("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
    
    table_data = []

    for table in tables_names:
        query = f'SELECT * FROM {table[0]} WHERE last_updated > :time;'
        updated_rows = con.run(query, time = latest_timestamp)

        column_names = [name["name"] for name in con.columns]

        if len(updated_rows) > 0:
            updated_rows.insert(0, column_names)

        table_data.append({table[0]: updated_rows})

    # for table in tables_names:
    #     if table[0] == "address" or table[0] == "department":
    #         full_table = f'SELECT * FROM {table[0]};'            
    #         table_rows = con.run(full_table)
            
    #         column_names = [name["name"] for name in con.columns]            

    #         table_rows.insert(0, column_names)
    #         table_data.append({f"full_{table[0]}_table": table_rows})

    for table_dict in table_data:
        for table_name in table_dict:
            if table_name == "address" or table_name == "department":
                if len(table_dict[table_name]) > 1:
                    full_table = f'SELECT * FROM {table_name};'            
                    table_rows = con.run(full_table)
                    
                    column_names = [name["name"] for name in con.columns]            
            
                    table_rows.insert(0, column_names)
                    table_data.append({f"full_{table_name}_table": table_rows})

    return table_data