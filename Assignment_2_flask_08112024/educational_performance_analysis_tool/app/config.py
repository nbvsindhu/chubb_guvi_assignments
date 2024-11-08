import os

class Config:
    SECRET_KEY = 'my_secret_key'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql://root:root123@localhost:3306')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True

config = Config()
