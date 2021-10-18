import os
from dotenv import load_dotenv
load_dotenv()
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
# Connect to the database


# TODO IMPLEMENT DATABASE URL
# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:boluwatife@localhost:5432/fyyur'
SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}/{}'.format(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)
print(SQLALCHEMY_DATABASE_URI)