import os
from flask import Flask, render_template
import firebase_admin
from firebase_admin import credentials, firestore
from app.routes import main  # Import the blueprint

# Flask-WTF for reCAPTCHA and CSRF protection
from flask_wtf.csrf import CSRFProtect
from flask_recaptcha import ReCaptcha  # For reCAPTCHA integration

# Import the configuration
from config import Config

# Initialize the Flask app
app = Flask(__name__, template_folder='templates')

# Load configuration from config.py
app.config.from_object(Config)

# Enable CSRF protection for the app
csrf = CSRFProtect(app)

# Initialize reCAPTCHA using the keys from the config
recaptcha = ReCaptcha(app)

# Path to the service account key JSON file for Firebase
cred = credentials.Certificate(os.path.join(os.path.dirname(__file__), app.config['FIREBASE_CREDENTIALS_PATH']))

# Initialize the Firebase Admin SDK (only once)
if not firebase_admin._apps:  # Avoid reinitialization if already initialized
    firebase_admin.initialize_app(cred)

# Initialize Firestore and store it in app configuration
app.config['db'] = firestore.client()

# Register the Blueprint after app and Firebase are set up
app.register_blueprint(main, url_prefix='/')

# Define a route for the index page
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
