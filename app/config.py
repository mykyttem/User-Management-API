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
TEST_DB_NAME = os.getenv("TEST_DB_NAME", "test_db_user_management")

# Build DATABASE_URL
def build_database_url(db_name):
    if DB_PASSWORD:
        return f"{DB_DIALECT}+{DB_DRIVER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{db_name}"
    return f"{DB_DIALECT}+{DB_DRIVER}://{DB_USER}@{DB_HOST}/{db_name}"

DATABASE_URL = build_database_url(DB_NAME)
TEST_DATABASE_URL = build_database_url(TEST_DB_NAME)

class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY')
    
    # SQLAlchemy settings
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = TEST_DATABASE_URL
    TESTING = False