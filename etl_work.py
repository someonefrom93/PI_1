from urllib.parse import quote_plus
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

user = "someone_from_93"
password = "rg550dx93"

uri = "mongodb+srv://" + user  +":" + password + "@cluster0.muda7ep.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client_atlas = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client_atlas.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client_atlas.pi_henry


def first_endpoint():
    return db.movies.find_one({})


