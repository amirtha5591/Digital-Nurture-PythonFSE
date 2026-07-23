import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'maleni_secret_key_123')
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///courses.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False