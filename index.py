from datetime import datetime
import random
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
client = MongoClient(db_url)
db = client['global']
chunkdata = db['chunkdata']

if __name__ == '__main__':
    app.run(debug=True,port=int(os.getenv('PORT', 5000)))  # Run the Flask app in debug mode