import pg8000

hostname='nc-data-eng-project-dw-prod.chpsczt8h1nu.eu-west-2.rds.amazonaws.com'
parole='5v8FmZSgQEdCxtN'
conn = pg8000.Connection(user='project_team_1',host=hostname,password=parole,database='postgres')
cursor = conn.cursor()
query = """
    SELECT attname, format_type(atttypid, atttypmod) AS data_type
    FROM pg_attribute
    WHERE attrelid = 'dim_date'::regclass AND attnum > 0
"""

cursor.execute(query)
results = cursor.fetchall()
for result in results:
    print(result)