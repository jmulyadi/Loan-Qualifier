import json
import os

from combine import *
from convert import *
from flask import Flask, jsonify, request
from flask_cors import CORS
from llm import *

app = Flask(__name__)

CORS(app)
# Set the upload folder and allowed file extensions
UPLOAD_FOLDER = "uploads/"
ALLOWED_EXTENSIONS = {"pdf"}

# Make sure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# Function to check the allowed file extension
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# Route to handle file upload
@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    if file and allowed_file(file.filename):
        # Secure the filename and save the file
        filename = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filename)
        # make LLM API call
        pdf_to_csv(file.filename)
        combine(f"csv/{file.filename[:-4]}")
        output = LLM()
        summary_score_json = get_score(output)
        data = json.loads(summary_score_json)
        return (
            jsonify(
                {
                    "message": f"File uploaded successfully",
                    "file_path": filename,
                    "score_summary_json": data,
                    "graph_data": json.loads(output),
                }
            ),
            200,
        )
    else:
        return jsonify({"error": "Invalid file type"}), 400


if __name__ == "__main__":
    app.run(
        ssl_context=("/app/certificate.crt", "/app/private.key"),
        # ssl_context=("../certificate.crt", "../private.key"),
        debug=True,
        host="0.0.0.0",
        port=5000,
    )
