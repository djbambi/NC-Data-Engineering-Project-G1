from db_connection import con

full_tables = ["address", "department"]


def get_sql_data(latest_timestamp):
    """ This function takes the latest time the ingested
    table was updated as an argument,
    then returns the date from the SQL database after that
    argument (latest time ingested table was updated)
    it returns a dictionary with
    a key of the table name and the a value
    of table data in a list that consists of nested lists that represent
    the rows of the table """

    tables_names = con.run(
        "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")

    table_data = {}

    for table in tables_names:
        query = f'SELECT * FROM {table[0]} WHERE last_updated > :time;'
        updated_rows = con.run(query, time=latest_timestamp)

        column_names = [name["name"] for name in con.columns]

        if len(updated_rows) < 0:
            continue

        updated_rows.insert(0, column_names)
        table_data[table[0]] = updated_rows

        if table[0] in full_tables:
            full_table = f'SELECT * FROM {table[0]};'
            updated_rows = con.run(full_table)
            column_names = [name["name"] for name in con.columns]
            updated_rows.insert(0, column_names)
            table_data[f"full_{table[0]}_table"] = updated_rows

    return table_data
