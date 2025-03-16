import os
from app.utils.logger import logger
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

# Load environment variables
load_dotenv()

# Get database connection parameters from .env
DB_DIALECT = os.getenv("DB_DIALECT", "mysql")
DB_DRIVER = os.getenv("DB_DRIVER", "pymysql")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "user_management")

# Build DATABASE_URL
if DB_PASSWORD:
    DATABASE_URL = f"{DB_DIALECT}+{DB_DRIVER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
else:
    DATABASE_URL = f"{DB_DIALECT}+{DB_DRIVER}://{DB_USER}@{DB_HOST}/{DB_NAME}"

logger.info(f"Connecting to database: {DATABASE_URL}")

# Initialize SQLAlchemy
db = SQLAlchemy()

# Check database connection and retrieve available databases and tables
try:
    engine = create_engine(DATABASE_URL)
    with engine.connect() as connection:
        logger.info(f"✅ Successfully connected to the database from {__file__}.")

        # Fetch available databases
        databases = connection.execute(text("SHOW DATABASES;")).fetchall()
        logger.info(f"📂 Available databases: {[db[0] for db in databases]}")

        # Fetch available tables in the selected database
        tables = connection.execute(text("SHOW TABLES;")).fetchall()
        logger.info(f"📋 Tables in {DB_NAME}: {[table[0] for table in tables]}")

except Exception as e:
    logger.error(f"❌ Failed to connect to database in {__file__}: {e}")