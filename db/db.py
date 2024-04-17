import os
import dotenv
from exceptions.error import Error
from formatters.db import from_db, to_db
from schemas.chunk_data import ChunkData, ChunkData_Base
from validators.validator import validate_chunk_data, validate_id
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

dotenv.load_dotenv()


db_url = os.getenv("DB_URL", "sqlite:///data.db")
db_name = os.getenv("DB", "chunkdata")

engine = create_engine(db_url)
ChunkData_Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


def insert(chunk_data):
    validate_chunk_data(chunk_data, with_id=True)
    session = Session()
    chunk_data = to_db(chunk_data)
    session.add(chunk_data)
    session.commit()
    chunk_data = from_db(chunk_data)
    session.close()
    validate_chunk_data(chunk_data, with_id=True)
    return chunk_data


def get_one(chunk_id):
    validate_id(chunk_id)
    session = Session()
    chunk_data = session.query(ChunkData).filter_by(_id=chunk_id).first()
    if chunk_data is None:
        return Error(f"Chunk data with id: {chunk_id} not found", 404)
    chunk_data = from_db(chunk_data)
    session.close()
    validate_chunk_data(chunk_data, with_id=True)
    return chunk_data
