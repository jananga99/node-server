from datetime import datetime
from flask import Flask, request, jsonify
import os
import dotenv
import db.db as db
import services.chunk_service as chunk_service

dotenv.load_dotenv()

app = Flask(__name__)

@app.route('/chunk', methods=['POST'])
def upload_chunk():
    try:
        inserted_chunk = chunk_service.insert(request.form['id'], request.form['chunk'], request.form['next_chunk_id'], request.form['next_chunk_node_id'])
        return jsonify(inserted_chunk)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/chunk/<chunk_id>', methods=['GET'])
def get_chunk_by_id(chunk_id):
    # try:
        chunk = chunk_service.get_one(chunk_id)
        return jsonify(chunk)
    # except Exception as e:
    #     return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True,port=int(os.getenv('PORT', 6000)))  # Run the Flask app in debug mode