import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'something'
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL") or "postgresql+psycopg2://postgres:password_weak@db:5432/flask_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
