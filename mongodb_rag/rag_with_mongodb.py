"""
https://www.mongodb.com/developer/products/atlas/parent-doc-retrieval/?utm_campaign=devrel&utm_source=youtube&utm_medium=organic_social&utm_content=v5V3W-NNSQw&utm_term=apoorva
"""
import os

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


def load_api_key_from_file(file_path="env.txt"):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} does not exist")

    with open(file_path, "r") as file:
        for line in file:
            key, value = line.strip().split("=", 1)
            os.environ[key] = value

def validate_mongodb_connection(mongodb_client):
    # Send a ping to confirm a successful connection
    try:
        mongodb_client.admin.command('ping')
        print("Pinged the deployment. You are successfully connected to MongoDB!")
    except Exception as e:
        print(e)

# Load the API keys into environment variables
load_api_key_from_file()


mongo_uri = f"{os.environ.get('MONGODB_URI')}?retryWrites=true&w=majority&appName=pixiehollow"
# Create a new client and connect to the server
client = MongoClient(mongo_uri, server_api=ServerApi('1'))
validate_mongodb_connection(client)
