from flask import Flask, request, jsonify
import boto3
import uuid
import json
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Initialize the S3 client
s3 = boto3.client('s3')
bucket_name = 'task-daxap-case'  # Replace with your bucket name

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the DAXAP API. Use /daxap/list, /daxap/put, or /daxap/get/<key>."

@app.route('/daxap/list', methods=['GET'])
def list_objects():
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
        objects = response.get('Contents', [])
        object_keys = [obj['Key'] for obj in objects]
        return jsonify(object_keys)
    except Exception as e:
        logging.error("Error listing objects: %s", e)
        return jsonify({'error': str(e)}), 500

@app.route('/daxap/put', methods=['POST'])
def put_object():
    try:
        data = request.get_json()
        object_key = str(uuid.uuid4()) + '.json'
        s3.put_object(Bucket=bucket_name, Key=object_key, Body=json.dumps(data))
        return jsonify({'key': object_key})
    except Exception as e:
        logging.error("Error putting object: %s", e)
        return jsonify({'error': str(e)}), 500

@app.route('/daxap/get/<key>', methods=['GET'])
def get_object(key):
    try:
        response = s3.get_object(Bucket=bucket_name, Key=key)
        content = response['Body'].read().decode('utf-8')
        return jsonify(json.loads(content))
    except s3.exceptions.NoSuchKey:
        return jsonify({'error': 'Key not found'}), 404
    except Exception as e:
        logging.error("Error getting object: %s", e)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
