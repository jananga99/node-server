import os
import dotenv
from pymongo import MongoClient

dotenv.load_dotenv()

db_url = os.getenv("DB_URL")
db_name = os.getenv("DB")
client = MongoClient(db_url)
db = client[db_name]
chunk_data_table = db["chunkdata"]


def insert(chunk_data):
    chunk_data["_id"] = chunk_data["id"]
    del chunk_data["id"]
    chunk_data_table.insert_one(chunk_data)
    chunk_data["id"] = str(chunk_data["_id"])
    del chunk_data["_id"]


def get_one(chunk_id):
    chunk_data = chunk_data_table.find_one({"_id": chunk_id})
    if chunk_data:
        chunk_data["id"] = str(chunk_data["_id"])
        del chunk_data["_id"]
        return chunk_data
    raise Exception("Chunk not found.")
