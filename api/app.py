import os
from flask import Flask, jsonify
from flask.json import JSONEncoder
from playhouse.flask_utils import FlaskDB

app = Flask(__name__)

# Loading the right configuration object
app.config.from_object('config.%sConfig' % os.environ.get('ENV', 'development').capitalize())

# Database Factory
db_wrapper = FlaskDB(app)
