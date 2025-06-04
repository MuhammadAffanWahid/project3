from flask import Flask
from pymongo import MongoClient
import os

DEFAULT_MONGO_URI = "mongodb+srv://affan:affan@deployment-test-cluster.rl1buzl.mongodb.net/?retryWrites=true&w=majority&appName=deployment-test-cluster"
client = MongoClient(os.getenv("MONGO_URI", DEFAULT_MONGO_URI))
db = client["userdb"]

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'
    app.db = db

    from .routes import main
    app.register_blueprint(main)

    return app
