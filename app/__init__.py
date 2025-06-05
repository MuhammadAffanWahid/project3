from flask import Flask
from pymongo import MongoClient
from .routes import main
import os
import certifi

DEFAULT_MONGO_URI = "mongodb+srv://affan:affan@deployment-test-cluster.rl1buzl.mongodb.net/?retryWrites=true&w=majority&appName=deployment-test-cluster"

def create_app():
    app = Flask(__name__)

    # Connect to MongoDB using environment variable
    mongo_url = os.getenv('MONGO_URI', DEFAULT_MONGO_URI)
    client = MongoClient(mongo_url,tls=True,tlsCAFile=certifi.where())
    app.db = client['flaskdb']

    app.register_blueprint(main)
    return app
