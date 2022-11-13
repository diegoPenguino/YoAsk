import os
DB_NAME = "database.db"
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'something'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or f"sqlite:///{os.path.join(basedir, DB_NAME)}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
