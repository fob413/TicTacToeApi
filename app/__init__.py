import os

from app.main import create_app


app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')

app.app_context().push()