import os

from flask import Flask, jsonify
from flask_cors import CORS

from pathlib import Path
from dotenv import load_dotenv
from app.main import create_app

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = create_app('dev')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv('PORT'))
