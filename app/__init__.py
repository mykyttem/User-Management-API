import os
from app.utils.logger import logger
from flask import Flask
from app.db.database import db
from dotenv import load_dotenv
from flask_migrate import Migrate

logger.info("Initializing the Flask app.")

def create_app():
    app = Flask(__name__)

    load_dotenv()

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate = Migrate(app, db)

    logger.info("🚀 Flask app initialized successfully.")
    logger.info(f"📡 Using database: {app.config['SQLALCHEMY_DATABASE_URI']}")

    return app