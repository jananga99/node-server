from datetime import datetime
import random
from bson import ObjectId
from flask import Flask, request, jsonify
from pymongo import MongoClient
from enum import Enum
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Connect to MongoDB
db_url = os.getenv("DB_URL")
db = os.getenv("DB")
print(db_url)
client = MongoClient(db_url)
db = client[db]
chunk_data_table = db['chunkdata']

@app.route('/chunk', methods=['POST'])
def upload_chunk():
    chunk_id = request.form['id']
    chunk = request.form['chunk']
    next_chunk_id = request.form['next_chunk_id']
    next_chunk_node_id = request.form['next_chunk_node_id']
    save_chunk({
        '_id': chunk_id,
        'chunk': chunk,
        'next_chunk_id': next_chunk_id,
        'next_chunk_node_id': next_chunk_node_id,
        'created_at': datetime.now()
    })
    return jsonify({'success': True, 'process': 'Chunk uploaded successfully.'})

@app.route('/chunk/<chunk_id>', methods=['GET'])
def get_chunk_by_id(chunk_id):
    chunk = get_chunk(chunk_id)
    if chunk:
        return jsonify({'success': True, 'data': chunk})
    return jsonify({'success': False, 'message': 'Chunk not found.'})

def save_chunk(chunk_data):
    chunk_data_table.insert_one(chunk_data)

def get_chunk(chunk_id):
    return chunk_data_table.find_one({'_id': chunk_id})

if __name__ == '__main__':
    app.run(debug=True,port=int(os.getenv('PORT', 6000)))  # Run the Flask app in debug mode