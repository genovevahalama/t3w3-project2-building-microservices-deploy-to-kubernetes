import json
import pymongo
import mysql.connector

# MongoDB connection settings
mongodb_host = "localhost"
mongodb_port = 27017
mongodb_database = "your_mongodb_database"
mongodb_collection = "your_mongodb_collection"

# MySQL connection settings
mysql_host = "localhost"
mysql_user = "your_mysql_user"
mysql_password = "your_mysql_password"
mysql_database = "your_mysql_database"

# Connect to MongoDB
mongodb_client = pymongo.MongoClient(mongodb_host, mongodb_port)
mongodb_db = mongodb_client[mongodb_database]
mongodb_collection = mongodb_db[mongodb_collection]

# Connect to MySQL
mysql_connection = mysql.connector.connect(
    host=mysql_host,
    user=mysql_user,
    password=mysql_password,
    database=mysql_database
)
mysql_cursor = mysql_connection.cursor()

# ETL Process
try:
    # Extract data from MongoDB
    mongo_data = mongodb_collection.find()

    # Transform and load data into MySQL
    for document in mongo_data:
        # Define your transformation logic here if needed
        id = document.get("id")
        name = document.get("name")
        description = document.get("description")

        # Prepare SQL query
        insert_query = "INSERT INTO your_mysql_table (id, name, description) VALUES (%s, %s, %s)"
        values = (id, name, description)

        # Execute the query
        mysql_cursor.execute(insert_query, values)
    
    # Commit changes to MySQL
    mysql_connection.commit()
    print("Data loaded into MySQL successfully.")

except Exception as e:
    print(f"Error: {e}")
finally:
    # Close MongoDB and MySQL connections
    mongodb_client.close()
    mysql_cursor.close()
    mysql_connection.close()
