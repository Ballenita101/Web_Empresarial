import os

class Config:
    SECRET_KEY = 'uhjk34b534538ddfsdf8'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAX_CONTENT_LENGTH = 24 * 1024 * 1024