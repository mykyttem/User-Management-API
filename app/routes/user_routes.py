from flask import jsonify, Blueprint
from flask_restx import Resource, Namespace, Resource, fields   
from app.controllers.user_controller import create_user, get_all_users, get_user_by_id, update_user, delete_user
from app.utils.logger import logger

user_bp = Blueprint('user', __name__)
user = Namespace("user", path="/users", description="User API controller")

def register_user_namespace(api):
    api.add_namespace(user)


user_post_model = user.model('User', {
    'name': fields.String(required=True, description='User name'),
    'email': fields.String(required=True, description='user@gmail.com')
})


@user.route('/users')
class UserList(Resource):
    """
    UserList: processing requests to the user list.
    """
    def get(self):
        """
        Getting all users
        """
        try:
            user_list = get_all_users()
            return jsonify(user_list)
        except Exception as e:
            logger.error(f"Error in UserList.get: {str(e)}")
            return jsonify({"message": "Something went wrong"})

    @user.expect(user_post_model)
    def post(self):
        """
        Create a new user
        """
        return create_user()


@user.route('/users/<int:user_id>')
class User(Resource):
    """
    User: processing requests to a specific user.
    """
    def get(self, user_id):
        """
        Getting a user by their ID
        """
        return get_user_by_id(user_id)

    @user.expect(user_post_model)
    def put(self, user_id):
        """
        Update a user by their ID
        """
        return update_user(user_id)

    def delete(self, user_id):
        """
        Delete a user by their ID
        """
        return delete_user(user_id)