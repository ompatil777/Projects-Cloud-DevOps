import boto3
import json
import logging
from flask import Flask, jsonify
from flask_cors import CORS
from botocore.exceptions import NoCredentialsError, ClientError

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Allow frontend requests

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize S3 client
try:
    s3 = boto3.client("s3")
except NoCredentialsError:
    logging.error("AWS credentials not found. Run 'aws configure' if needed.")

# Your bucket name
bucket_name = "YOUR-BUCKET-NAME"

@app.route("/list-files", methods=["GET"])
def list_s3_objects():
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)

        if "Contents" in response:
            files = [obj["Key"] for obj in response["Contents"]]  # ✅ Fixed syntax
            return jsonify({"files": files})
        else:
            return jsonify({"files": []})  # ✅ Returns empty list if no files

    except ClientError as e:
        logging.error(f"Error fetching S3 files: {e}")
        return jsonify({"error": "Failed to retrieve files"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)