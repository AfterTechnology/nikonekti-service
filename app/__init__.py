from flask import Flask
from pymongo import MongoClient

def create_app():
    # Creating flask app instance
    app = Flask(__name__, template_folder='templates')

    # importing blueprints
    from app.blueprints.root import index

    # Registering blueprints
    app.register_blueprint(index.bp)

    return app

def get_db():
    client = MongoClient('mongodb://localhost:27017/')
    return client.customer_service_db