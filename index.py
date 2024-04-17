from flask import Flask, request, jsonify
import os
import dotenv
import services.chunk_service as chunk_service
from exceptions.error import Error
from formatters.chunk import to_str_chunk, to_byte_chunk

dotenv.load_dotenv()

app = Flask(__name__)


@app.route("/chunk", methods=["POST"])
def upload_chunk():
    try:
        data = request.get_json()
        inserted_chunk = chunk_service.insert(
            data["id"],
            to_byte_chunk(data["chunk"]),
            data["next_chunk_id"],
            str(data["next_chunk_node_id"]),
        )
        inserted_chunk["chunk"] = to_str_chunk(inserted_chunk["chunk"])
        return jsonify(inserted_chunk)
    except Error as e:
        print(f"Error: {e.message}")
        return jsonify({"error": e.message}), e.status_code
    except Exception as e:
        print("Unexpected error occured", e)
        return jsonify({"error": "Unexpected error occured"}), 500


@app.route("/chunk/<chunk_id>", methods=["GET"])
def get_chunk_by_id(chunk_id):
    try:
        chunk_data = chunk_service.get_one(chunk_id)
        chunk_data["chunk"] = to_str_chunk(chunk_data["chunk"])
        return jsonify(chunk_data)
    except Error as e:
        print(f"Error: {e.message}")
        return jsonify({"error": e.message}), e.status_code
    except Exception as e:
        print("Unexpected error occured", e)
        return jsonify({"error": "Unexpected error occured"}), 500


if __name__ == "__main__":
    app.run(
        debug=True, port=int(os.getenv("PORT", 6000))
    )  # Run the Flask app in debug mode
