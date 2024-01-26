from sqlalchemy import create_engine
import json
import pymongo
import mysql.connector
import pandas as pd

# MySQL connection settings
mysql_host="mysql-container"
mysql_user = "admin"
mysql_password = "admin"
mysql_database = "hogwarts"
mysql_engine = create_engine(f'mysql+pymysql://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_database}')
 
mongodb_host="mongodb-container"
mongodb_port=27017
mongodb_database="hogwarts"
 
# Connect to MongoDB
mongodb_client = pymongo.MongoClient(mongodb_host, mongodb_port)
mongodb_db = mongodb_client[mongodb_database]
col_spells = mongodb_db["spells"]
col_stuff = mongodb_db["stuff"]
 
# Connect to MySQL
mysql_connection = mysql.connector.connect(
    host=mysql_host,
    user=mysql_user,
    password=mysql_password,
    database=mysql_database
)

#for doc in col_spells.find():   
 #   print("stells:",doc)
 
df = pd.DataFrame(col_spells.find())
df=df.drop(columns=['_id'])
df=df.drop(columns=['id'])
print("columns:",df.columns)
df.to_sql("Spells", con=mysql_engine, if_exists='replace', index=False)

df = pd.DataFrame(col_stuff.find())
df=df.drop(columns=['_id'])
df=df.drop(columns=['id'])
print("columns:",df.columns)
df.to_sql("Characters", con=mysql_engine, if_exists='replace', index=False)


 
print("Data transfer complete.")
