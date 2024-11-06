import os
from flask import Flask, render_template, request
import firebase_admin
from firebase_admin import credentials

# Initialize the Flask app
app = Flask(__name__)

# Path to the service account key JSON file
cred = credentials.Certificate(os.path.join(os.path.dirname(__file__), 'serviceAccountKey.json'))

# Initialize the Firebase Admin SDK
firebase_admin.initialize_app(cred)

# Import the main blueprint
from app.routes import main

# Register the blueprint
app.register_blueprint(main)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    # Save registration details or send an email
    return "Registration Successful!"

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    # Process contact form submission
    return "Message Sent!"

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)



