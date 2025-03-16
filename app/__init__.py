from flask import Flask
from flask_migrate import Migrate
from app.utils.logger import logger
from app.db.database import db
from app.config import Config
from sqlalchemy.exc import OperationalError
from dotenv import load_dotenv

# Import the User model to make it available to Alembic
from app.models.user import User

load_dotenv()

logger.info("Initializing the Flask app.")

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    migrate = Migrate()
    db.init_app(app)
    migrate.init_app(app, db)

    try:
        logger.info(f"Checking database connection in app/{__file__}")
        
        # A simple SQL query to check the connection
        with app.app_context():
            db.engine.connect()

        logger.info("✅ Database connection is successful for initializing the flask app.")
    except OperationalError as e:
        logger.error(f"❌ Failed to connect to the database in {__file__}: {e}")
        raise e


    logger.info("🚀 Flask app initialized successfully.")
    logger.info(f"📡 Using database: {app.config['SQLALCHEMY_DATABASE_URI']}")

    return app