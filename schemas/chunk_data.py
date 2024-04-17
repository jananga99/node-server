import uuid
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

ChunkData_Base = declarative_base()


class ChunkData(ChunkData_Base):
    __tablename__ = "chunkdata"
    _id = Column(String, primary_key=True, default=str(uuid.uuid4().hex))
    chunk = Column(String)
    next_chunk_id = Column(String)
    next_chunk_node_id = Column(Integer)
    created_at = Column(String)
