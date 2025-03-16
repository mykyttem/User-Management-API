from app.models.user import User

class UserService:
    def __init__(self):
        pass
    
    def create_user(self, name, email):
        if User.query.filter_by(email=email).first():
            raise ValueError("Email already exists")
        return User.create(name, email)
    
    def get_all_users(self):
        return User.query.all()