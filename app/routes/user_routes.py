from flask import Blueprint
from app.controllers.user_controller import create_user, get_all_users

user_bp = Blueprint('user', __name__)


user_bp.route("/", methods=["POST"])(create_user)
user_bp.route("/", methods=["GET"])(get_all_users)