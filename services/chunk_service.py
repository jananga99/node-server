from datetime import datetime
import db.db as db
from validators.validator import validate_chunk_data, validate_chunk, validate_id


def insert(chunk_id, chunk, next_chunk_id, next_chunk_node_id):
    validate_id(chunk_id)
    validate_id(next_chunk_id)
    validate_id(next_chunk_node_id)
    validate_chunk(chunk)
    inserted_chunk = db.insert(
        {
            "id": chunk_id,
            "chunk": chunk,
            "next_chunk_id": next_chunk_id,
            "next_chunk_node_id": next_chunk_node_id,
            "created_at": datetime.now(),
        }
    )
    validate_chunk_data(inserted_chunk, with_id=True)
    return inserted_chunk


def get_one(chunk_id):
    validate_id(chunk_id)
    chunk = db.get_one(chunk_id)
    validate_chunk_data(chunk, with_id=True)
    return chunk


def delete(chunk_id):
    validate_id(chunk_id)
    chunk = db.delete(chunk_id)
    validate_chunk_data(chunk, with_id=True)
    return chunk
