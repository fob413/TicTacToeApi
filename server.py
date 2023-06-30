import os

from flask import Flask, jsonify
from flask_cors import CORS

from pathlib import Path
from dotenv import load_dotenv
from config import app_configuration
from app.main import create_app

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


# # function that creates the flask app, initializes the db and sets the routes
# def create_flask_app(environment):
#     app = Flask(__name__, instance_relative_config=True, static_folder=None, template_folder='./emails/templates')
#
#     # enable CORS
#     cors = CORS(app, resources={r"/*": {"origins": "*"}})
#     app.config.from_object(app_configuration[environment])
#     app.config['BUNDLE_ERRORS'] = True
#
#     # landing route
#     @app.route('/')
#     def index():
#         return "TUA Backend"
#
#     # initialize api resources
#     api.init_app(app)
#
#     # handle default 404 exceptions with a custom response
#     @app.errorhandler(404)
#     def resource_not_found(exception):
#         response = jsonify(dict(status='fail', data={
#             'error': 'Not found', 'message': 'The requested URL was'
#                                              ' not found on the server. If you entered the URL '
#                                              'manually please check and try again'
#         }))
#         response.status_code = 404
#         return response
#
#     # both error handlers below handle default 500 exceptions with a custom
#     # response
#     @app.errorhandler(500)
#     def internal_server_error(error):
#         response = jsonify(dict(status=error, error='Internal Server Error',
#                                 message='The server encountered an internal error and was'
#                                         ' unable to complete your request.  Either the server is'
#                                         ' overloaded or there is an error in the application'))
#         response.status_code = 500
#         return response
#
#     environment = os.getenv('FLASK_CONFIG')
#
#     return app



# starts the flask application
app = create_app('dev')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv('PORT'))
