from flask import Flask

from app.api_1_0 import api
from app.model import db
from config import config


def create_app(config_name=None):
    flask_app = Flask(__name__)
    flask_app.config.from_object(config[config_name])

    db.init_app(flask_app)

    flask_app.register_blueprint(api, url_prefix="/api/v1.0")
    return flask_app

