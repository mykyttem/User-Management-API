from flask import jsonify, request
from app.services.user_service import UserService

def create_user():
    try:
        data = request.get_json()

        if not data.get('name') or not data.get('email'):
            return jsonify({"message": "Name and email are required"}), 400

        user_service = UserService()
        user = user_service.create_user(data['name'], data['email'])
        
        return jsonify(user.to_dict()), 201
    except ValueError as e:
        return jsonify({"message": str(e)}), 400
    except Exception as e:
        return jsonify({"message": "Something went wrong"}), 500