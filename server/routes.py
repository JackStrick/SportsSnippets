from flask import Blueprint
from controllers.user_controller import users

api = Blueprint('api', __name__)

api.register_blueprint(users, url_prefix="/users")