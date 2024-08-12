from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
# Allow cross-origin requests to API
CORS(app) 

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sportssnippets.db"
 # Currently not tracking changeds/modifications
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# DB instance ORM
db = SQLAlchemy(app)




