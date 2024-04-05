from datetime import datetime
import db.db as db


def insert(chunk_id, chunk, next_chunk_id, next_chunk_node_id):
    inserted_chunk = db.insert(
        {
            "id": chunk_id,
            "chunk": chunk,
            "next_chunk_id": next_chunk_id,
            "next_chunk_node_id": next_chunk_node_id,
            "created_at": datetime.now(),
        }
    )
    return inserted_chunk


def get_one(chunk_id):
    chunk = db.get_one(chunk_id)
    return chunk
