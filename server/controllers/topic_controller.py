from flask import request, Response, jsonify, Blueprint, json
from models.topics import Topic
from config import bcrypt, db
from datetime import datetime
import jwt
import os

topics = Blueprint("topics", __name__)

@topics.route("/", methods=["GET"])
def get_users():
    topics = Topic.query.all()
    json_topics = list(map(lambda x: x.to_json(), topics))
    return jsonify({"topics": json_topics})
