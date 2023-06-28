import os

from urllib.parse import quote_plus
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from dotenv import load_dotenv

load_dotenv()

user = os.environ.get("USER")
password = os.environ.get("PASSWORD")

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

movies = db.movies

##############################################################################

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def execute_query():
    result = movies.find_one({})
    data = [movie for movie in result]
    return {"data": data}





