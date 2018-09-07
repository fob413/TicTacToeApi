from flask import Flask
from flask_restful import Api
from flask_bcrypt import Bcrypt
from app.main.controller.game import Game


from .config import config_by_name


flask_bcrypt = Bcrypt()


def create_app(config_name):
    app = Flask(__name__)
    api = Api(app)
    app.config.from_object(config_by_name[config_name])
    flask_bcrypt.init_app(app)

    api.add_resource(Game, '/')

    return app
