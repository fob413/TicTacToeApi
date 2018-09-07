import os

from app import app
from flask_script import Manager
from app.main import create_app


manager = Manager(app)

@manager.command
def run():
    app.run()


if __name__ == '__main__':
    manager.run()
