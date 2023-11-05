import pymongo
import os

from flask import Flask
from flask import request, jsonify
from flask_cors import CORS

# Define the path to your .env file
env_file = '.env'

# Check if the .env file exists
if os.path.exists(env_file):
    # Read and parse the .env file
    with open(env_file, 'r') as file:
        for line in file:
            # Split each line into key-value pairs
            key, value = line.strip().split('=', 1)

            # Set the environment variable (this makes it accessible via os.environ)
            os.environ[key] = value

# Now you can access the configuration variables
MONGO_URI = os.environ.get("MONGO_URI")

client = pymongo.MongoClient(os.environ.get('ATLAS_URI'))
db = client[os.environ.get('DB_NAME')]
cul = db['cc']

app = Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/push', methods = ['Post', 'Get'])
def push():
  print('pushing something')

@app.route('/pull', methods = ['Post', 'Get'])
def pull():
  print('pulling something')