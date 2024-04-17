from schemas.chunk_data import ChunkData


def from_db(chunk_data):
    return {
        "id": str(chunk_data._id),
        "chunk": chunk_data.chunk,
        "next_chunk_id": chunk_data.next_chunk_id,
        "next_chunk_node_id": chunk_data.next_chunk_node_id,
        "created_at": chunk_data.created_at,
    }


def to_db(chunk_data):
    chunk_data["_id"] = chunk_data["id"]
    del chunk_data["id"]
    return ChunkData(**chunk_data)
