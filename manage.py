import os
import unittest

from flask.cli import FlaskGroup
from app import app
from app.main import create_app


cli = FlaskGroup(app)


@app.shell_context_processor
@cli.command('run')
def run():
    app.run()


@app.shell_context_processor
@cli.command('test')
def test():
    """Runs the unit tests"""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)

    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    cli()
