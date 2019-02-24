import os
from flask import Flask

from .config import config
from .db import db
from .security import jwt
from .apis import api


def config_app(app, config_obj):
    config_name = os.getenv('FLASK_CONFIGURATION', 'default')
    app.config.from_object(config[config_name])
    app.config.from_pyfile('config.cfg', silent=True)
    if config_obj is not None:
        app.config.from_mapping(config_obj)


def create_server(config_obj=None):
    app = Flask(__name__, instance_relative_config=False)
    config_app(app, config_obj)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    #

    db.init_app(app)
    jwt.init_app(app)
    api.init_app(app)


    @app.before_first_request
    def create_tables():
        db.create_all()

    print('**** app created')
    return app
