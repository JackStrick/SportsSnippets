from flask import request, jsonify
from config import app, db
from models.users import User
from models.topics import Topic
from models.favorited_topics import FavoritedTopic
#from models.sources import Sourcest 
from models.summaries import Summary

@app.route("/")
def hello():
    return "Welcome to Sports Snippets"





if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)