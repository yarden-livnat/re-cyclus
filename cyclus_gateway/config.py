"""Application configuration."""
import os
from datetime import timedelta

class Config(object):
    SECRET_KEY = os.environ.get('CYCLUS_GATEWAY_SECRET', 'gateway-dev-secret')
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    BCRYPT_LOG_ROUNDS = 13
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = 'cyclus-services-secret'  # Change this and remove from config
    JWT_AUTH_USERNAME_KEY = 'email'
    JWT_TOKEN_LOCATION = ['headers'] #'cookies']

    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']

    # JWT_ACCESS_COOKIE_PATH = '/api/'
    # JWT_REFRESH_COOKIE_PATH = '/token/refresh'

class ProdConfig(Config):
    ENV = 'prod'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'  # change
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=15)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)


class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True
    DB_NAME = 'dev.db'
    DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB_PATH}'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=15)
    # Only allow JWT cookies to be sent over https. In production, this
    # should likely be True
    JWT_COOKIE_SECURE = False
    # Disable CSRF protection for this example. In almost every case,
    # this is a bad idea. See examples/csrf_protection_with_cookies.py
    # for how safely store JWTs in cookies
    JWT_COOKIE_CSRF_PROTECT = False


class TestConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    # For faster tests; needs at least 4 to avoid "ValueError: Invalid rounds"
    BCRYPT_LOG_ROUNDS = 4
    # Only allow JWT cookies to be sent over https. In production, this
    # should likely be True
    JWT_COOKIE_SECURE = False
    # Disable CSRF protection for this example. In almost every case,
    # this is a bad idea. See examples/csrf_protection_with_cookies.py
    # for how safely store JWTs in cookies
    JWT_COOKIE_CSRF_PROTECT = False

config = {
    "prod": ProdConfig,
    "dev": DevConfig,
    "testing": TestConfig,
    "default": DevConfig
}
