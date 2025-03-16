from app.models.user import User
from app.db.database import db


class UserService:
    def __init__(self):
        pass
    
    def create_user(self, name, email):
        if User.query.filter_by(email=email).first():
            raise ValueError("Email already exists")
        return User.create(name, email)
    
    def get_all_users(self):
        return User.query.all()

    def get_user_by_id(self, user_id):
        return User.query.get(user_id)
    
    def update_user(self, user_id, name, email):
        user = User.query.get(user_id)
        
        if not user:
            raise ValueError("User not found")
        
        # Update user details
        user.name = name
        user.email = email
        db.session.commit()
        
        return user