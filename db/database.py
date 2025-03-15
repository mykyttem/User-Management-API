from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Getting variables from .env
load_dotenv()

DB_DIALECT = os.getenv("DB_DIALECT", "mysql")
DB_DRIVER = os.getenv("DB_DRIVER", "pymysql")
DB_USER = os.getenv("DB_USER", "user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "db_name")

# Formation of DATABASE_URL
DATABASE_URL = f"{DB_DIALECT}+{DB_DRIVER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# Checking if a variable is not empty
if not all([DB_USER, DB_PASSWORD, DB_HOST, DB_NAME]):
    raise ValueError("One or more database environment variables are missing in .env file")

# Setting up SQLAlchemy
engine = create_engine(DATABASE_URL)
Base = declarative_base()
db = SQLAlchemy()