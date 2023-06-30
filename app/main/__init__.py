from flask import Flask
from flask_restful import Api
from app.main.controller.game import Game


from .config import config_by_name


def create_app(config_name):
    app = Flask(__name__)
    api = Api(app)
    app.config.from_object(config_by_name[config_name])

    api.add_resource(Game, '/')

    return app
