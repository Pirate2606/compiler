import os

class Config(object):
    SECRET_KEY = "supersekrit"
    SQLALCHEMY_DATABASE_URI = "sqlite:///app.sqlite3"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    GOOGLE_OAUTH_CLIENT_ID = YOUR_ID_HERE
    GOOGLE_OAUTH_CLIENT_SECRET = YOUR_SECRET_KEY
