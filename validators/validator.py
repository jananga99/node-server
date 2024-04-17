from exceptions.error import Error


# TODO - Add validators for chunk
def validate_chunk(chunk):
    return chunk


def validate_chunk_data(chunk_data, with_id=False, with_db_id=False):
    if type(chunk_data) is not dict:
        print(chunk_data)
        raise Error(f"Chunk data is not a dictionary but {type(chunk_data)}", 500)
    if with_id and "id" not in chunk_data:
        raise Error("id is required in chunk data", 500)
    if with_db_id and "_id" not in chunk_data:
        raise Error("_id is required in chunk data", 500)
    if "chunk" not in chunk_data:
        raise Error("chunk is required in chunk data", 500)
    else:
        validate_chunk(chunk_data["chunk"])
    if "next_chunk_id" not in chunk_data:
        raise Error("next_chunk_id is required in chunk data", 500)
    if "next_chunk_node_id" not in chunk_data:
        raise Error("next_chunk_node_id is required in chunk data", 500)
    return chunk_data


# TODO - Add validators for chunk
def validate_chunk(chunk):
    return chunk


def validate_id(id):
    if type(id) is not str:
        raise Error(f"id: {id} is not a string, but {type(id)}", 500)
    return id
