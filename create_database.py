import os
from sqlalchemy import create_engine
db_user = os.environ['PG_USER']
db_pass = os.environ['PG_PASS']

# Create the database
engine = create_engine("postgresql+psycopg2://{}:{}@localhost/postgres".format(db_user,db_pass))
conn = engine.connect()
conn.execute("commit")
conn.execute("create database covermymeds")
conn.close()

import populate_database
populate_database.run_all()
