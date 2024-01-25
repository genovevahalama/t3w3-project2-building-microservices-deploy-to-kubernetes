import pymongo
import json
import requests

def fetch_jsondata():
  url = "https://hp-api.onrender.com/api/characters/staff"
  response = requests.get(url)
  if response.status_code == 200:
          #print(response.json())
          jsondata = response.json()
          return jsondata  #json object to be saved
  else:
          return "Error: " + str(response.status_code)

json_hogwarts_stuff = fetch_jsondata()
print(type(json_hogwarts_stuff))
print(json_hogwarts_stuff)

# MongoDB connection string Format: mongodb://username:password@host:port/database
connection_string = "mongodb://mongodb-container:27017/testdb"
client = pymongo.MongoClient(connection_string)

try:
    client.admin.command('ismaster')
    print("MongoDB connection successful")
except Exception as e:
    print("Error connecting to MongoDB:", e)

# Select your database
db = client.characters

# Select the collection
collection = db.characterscollection

# JSON data
json_data =json_hogwarts_stuff
print("JSON data to be stored: ",json_data)

# Insert JSON data into MongoDB
if isinstance(json_data, list):
    collection.insert_many(json_data)
elif isinstance(json_data, dict):
    collection.insert_one(json_data)
else:
    print("Error: json_data is neither a list nor a dictionary")

print("JSON data inserted successfully")

for doc in collection.find():
    print(doc)