from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

load_dotenv()

app = Flask(__name__)
# Allow cross-origin requests to API
CORS(app) 

bcrypt = Bcrypt(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sportssnippets.db"
 # Currently not tracking changeds/modifications
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# DB instance ORM
db = SQLAlchemy(app)

from routes import api
app.register_blueprint(api, url_prefix="/api")


