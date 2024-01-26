import pymongo
import json
import requests

spells_url="https://hp-api.onrender.com/api/spells"
stuff_url="https://hp-api.onrender.com/api/characters/staff"

def fetch_jsondata(url):
  response = requests.get(url)
  if response.status_code == 200:
          #print(response.json())
          jsondata = response.json()
          return jsondata  #json object to be saved
  else:
          return "Error: " + str(response.status_code)

list_stuff = fetch_jsondata(stuff_url)
list_spells = fetch_jsondata(spells_url)
print("stuff: ", list_stuff)
print("spells: ",list_spells)

# MongoDB connection string Format: mongodb://username:password@host:port/database
connection_string = "mongodb://mongodb-container:27017/testdb"
client = pymongo.MongoClient(connection_string)

try:
    client.admin.command('ismaster')
    print("MongoDB connection successful")
except Exception as e:
    print("Error connecting to MongoDB:", e)

# Select your database
db = client['hogwarts']

db['stuff'].insert_many(list_stuff)
db['spells'].insert_many(list_spells)

def print_collection(collection_name):
    collection = db[collection_name]
    for doc in collection.find():
        print(doc)

print("Stuff Collection:")
print_collection('stuff')

print("\nSpells Collection:")
print_collection('spells')

client.close()