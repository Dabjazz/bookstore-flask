from flask import Flask
from config_template import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)
auth = HTTPBasicAuth()
CORS(app)

from app import routes, models
