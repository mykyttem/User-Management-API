from flask import jsonify, request
from app.services.user_service import UserService
from app.utils.logger import logger

def create_user():
    """
    Creates a new user.
    Expects JSON with the 'name' and 'email' fields.
    If the fields are not provided, it returns an error.
    """
    try:
        data = request.get_json()

        if not data.get('name') or not data.get('email'):
            return jsonify({"message": "Name and email are required"})
        
        user_service = UserService()
        user = user_service.create_user(data['name'], data['email'])

        return jsonify(user.to_dict())
    except ValueError as e:
        return jsonify({"message": str(e)})
    except Exception as e:
        return jsonify({"message": "Something went wrong"})


def get_all_users():
    try:
        user_service = UserService()
        users = user_service.get_all_users()

        user_list = []
        for user in users:
            user_dict = {
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'created_at': user.created_at.strftime('%Y-%m-%dT%H:%M:%S')
            }
            user_list.append(user_dict)


        return user_list

    except Exception as e:
        logger.error(f"Error in get_all_users: {str(e)}")
        return []
   

def get_user_by_id(user_id):
    try:
        user_service = UserService()
        user = user_service.get_user_by_id(user_id)
        
        if user:
            return jsonify(user.to_dict())
        else:
            return jsonify({"message": "User not found"})
    except Exception as e:
        logger.error(f"Error in get_user_by_id: {str(e)}")
        return jsonify({"message": "Something went wrong"})
   

def update_user(user_id):
    try:
        data = request.get_json()

        if not data.get('name') or not data.get('email'):
            return jsonify({"message": "Name and email are required"})

        user_service = UserService()
        user = user_service.update_user(user_id, data['name'], data['email'])
        
        return jsonify(user.to_dict())
    except ValueError as e:
        return jsonify({"message": str(e)})
    except Exception as e:
        logger.error(f"Error in update_user: {str(e)}")
        return jsonify({"message": "Something went wrong"})


def delete_user(user_id):
    try:
        user_service = UserService()
        user = user_service.get_user_by_id(user_id)
        
        if user:
            user_service.delete_user(user_id)
            return jsonify({"message": "User deleted successfully"})
        else:
            return jsonify({"message": "User not found"})
    except Exception as e:
        logger.error(f"Error in delete_user: {str(e)}")
        return jsonify({"message": "Something went wrong"})