import pg8000.native as pg

# Totesys connection variables:
host = "nc-data-eng-totesys-production.chpsczt8h1nu.eu-west-2.rds.amazonaws.com"
port = 5432
database = 'totesys'
user = 'project_user_1'
password = 'Zwec2EPvgedMGtT9ATGQFnDz'

# API Connection
con = pg.Connection(user, host=host, database='totesys', password=password)
