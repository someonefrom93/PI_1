import os

from urllib.parse import quote_plus
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from dotenv import load_dotenv

load_dotenv()

USER = os.environ.get("USER")
PASSWORD = os.environ.get("PASSWORD")

uri = "mongodb+srv://" + str(USER)  + ":" + str(PASSWORD) + "@cluster0.muda7ep.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client_atlas = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client_atlas.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)