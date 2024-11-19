import os

class Config:
    # Secret key for CSRF protection and Flask-WTF
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')  # Default to 'your_secret_key' if not set in environment
    DEBUG = os.getenv('FLASK_DEBUG', 'True') == 'True'  # Set debug mode from environment variable if available

    # Google reCAPTCHA keys
    RECAPTCHA_PUBLIC_KEY = os.getenv('RECAPTCHA_PUBLIC_KEY', 'your_site_key')  # Replace with actual public key or use environment variable
    RECAPTCHA_PRIVATE_KEY = os.getenv('RECAPTCHA_PRIVATE_KEY', 'your_secret_key')  # Replace with actual secret key or use environment variable

    # Firebase configuration
    FIREBASE_CREDENTIALS_PATH = os.getenv('FIREBASE_CREDENTIALS_PATH', 'serviceAccountKey.json')  # Path to your Firebase service account JSON file
