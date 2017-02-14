import os
from peewee import MySQLDatabase, SqliteDatabase


class BaseConfig(object):
    DEBUG = True
    TESTING = False
    DATABASE = os.environ.get('DATABASE_CONNECTION_STRING', 'sqlite:///:memory:')


class DevelopmentConfig(BaseConfig):
    DATABASE = 'sqlite:///users.db'


class ProductionConfig(BaseConfig):
    DEBUG = False


class TestConfig(BaseConfig):
    TESTING = True
