from flask import Blueprint
from controllers.user_controller import users
from controllers.story_controller import stories
from controllers.summary_controller import summaries
from controllers.topic_controller import topics

api = Blueprint('api', __name__)

api.register_blueprint(users, url_prefix="/users")
api.register_blueprint(stories, url_prefix="/stories")
api.register_blueprint(summaries, url_prefix="/summaries")
api.register_blueprint(topics, url_prefix="/topics")