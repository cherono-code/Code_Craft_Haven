from flask import Flask
from config import Config
from app.routes import main  # Import the blueprint

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(main)  # Register the blueprint



