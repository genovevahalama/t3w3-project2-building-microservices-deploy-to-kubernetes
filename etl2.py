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
 
# Connect to MongoDB
mongodb_client = pymongo.MongoClient(mongodb_host, mongodb_port)
mongodb_db = mongodb_client[mysql_database]
mongodb_collection = mongodb_db[mysql_database]

 
# Connect to MySQL
mysql_connection = mysql.connector.connect(
    host=mysql_host,
    user=mysql_user,
    password=mysql_password,
    database=mysql_database
)
mysql_cursor = mysql_connection.cursor()
 
for collection_name in mongodb_db.list_collection_names():
    
    print("collection_name:",collection_name)
    if collection_name == "Spells":
        collection = mongodb_db[collection_name]
        #data = list(collection.find())
        print("df: ",df)
        print("collection: ",collection)
        df = pd.DataFrame(collection)
        df=df.drop(columns=['_id'])
        df=df.drop(columns=['id'])
        df.to_sql('Spells', con=mysql_engine, if_exists='append', index=False)
    #df_weather.to_sql('weather', con=engine, if_exists='append', index=False)
    if collection_name == "Characters":
        collection = mongodb_db[collection_name]
        #data = list(collection.find())
        print("df: ",df)
        print("collection: ",collection)
        df = pd.DataFrame(collection)
        df=df.drop(columns=['_id'])
        df=df.drop(columns=['id'])
        df.to_sql('Characters', con=mysql_engine, if_exists='append', index=False)
 
print("Data transfer complete.")
