import os
import dotenv
from pymongo import MongoClient
from formatters.db import from_db, to_db
from validators.validator import validate_chunk_data, validate_id

dotenv.load_dotenv()

db_url = os.getenv("DB_URL")
db_name = os.getenv("DB")
client = MongoClient(db_url)
db = client[db_name]
chunk_data_table = db["chunkdata"]


def insert(chunk_data):
    validate_chunk_data(chunk_data, with_id=True)
    to_db(chunk_data)
    chunk_data_table.insert_one(chunk_data)
    validate_chunk_data(chunk_data, with_db_id=True)
    from_db(chunk_data)
    return chunk_data


def get_one(chunk_id):
    validate_id(chunk_id)
    chunk_data = chunk_data_table.find_one({"_id": chunk_id})
    validate_chunk_data(chunk_data, with_db_id=True)
    from_db(chunk_data)
    return chunk_data
