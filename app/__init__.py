import os
from flask import Flask
import firebase_admin
from firebase_admin import credentials, firestore

def create_app():
    app = Flask(__name__)

    # Load configuration from config.py
    app.config.from_object('config.Config')

    # Path to the service account key JSON file
    cred_path = os.path.join(os.path.dirname(__file__), '../serviceAccountKey.json')
    cred = credentials.Certificate(cred_path)
    
    # Initialize Firebase Admin SDK only if not already initialized
    if not firebase_admin._apps:
        firebase_admin.initialize_app(cred)
    
    # Initialize Firestore and add it to the app config
    app.config['db'] = firestore.client()

    # Import and register the main blueprint
    from app.routes import main
    app.register_blueprint(main)

    return app
