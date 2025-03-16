import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv()

# Load environment variables
load_dotenv()

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

class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY')
    
    # SQLAlchemy settings
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False