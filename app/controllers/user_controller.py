from flask import jsonify, request
from app.services.user_service import UserService
from app.utils.logger import logger

def create_user():
    try:
        data = request.get_json()

        # Basic validation for name and email fields
        if not data.get('name') or not data.get('email'):
            return jsonify({"message": "Name and email are required"}), 400
        
        user_service = UserService()
        user = user_service.create_user(data['name'], data['email'])
        
        return jsonify(user.to_dict()), 201
    except ValueError as e:
        return jsonify({"message": str(e)}), 400
    except Exception as e:
        return jsonify({"message": "Something went wrong"}), 500


def get_all_users():
    try:
        user_service = UserService()
        users = user_service.get_all_users()

        return jsonify([user.to_dict() for user in users]), 200
    except Exception as e:
        logger.error(f"Error in get_all_users: {str(e)}")
        return jsonify({"message": "Something went wrong"}), 500
   

def get_user_by_id(user_id):
    try:
        user_service = UserService()
        user = user_service.get_user_by_id(user_id)
        
        if user:
            return jsonify(user.to_dict()), 200
        else:
            return jsonify({"message": "User not found"}), 404
    except Exception as e:
        logger.error(f"Error in get_user_by_id: {str(e)}")
        return jsonify({"message": "Something went wrong"}), 500
   

def update_user(user_id):
    try:
        data = request.get_json()

        # Basic validation for name and email fields
        if not data.get('name') or not data.get('email'):
            return jsonify({"message": "Name and email are required"}), 400

        user_service = UserService()
        user = user_service.update_user(user_id, data['name'], data['email'])
        
        return jsonify(user.to_dict()), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 400
    except Exception as e:
        logger.error(f"Error in update_user: {str(e)}")
        return jsonify({"message": "Something went wrong"}), 500


def delete_user(user_id):
    try:
        user_service = UserService()
        user = user_service.get_user_by_id(user_id)
        
        if user:
            user_service.delete_user(user_id)
            return jsonify({"message": "User deleted successfully"}), 200
        else:
            return jsonify({"message": "User not found"}), 404
    except Exception as e:
        logger.error(f"Error in delete_user: {str(e)}")
        return jsonify({"message": "Something went wrong"}), 500