from datetime import datetime
from app.db.database import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.name}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'created_at': self.created_at
        }

    @classmethod
    def create(cls, name, email):
        new_user = cls(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()
        return new_user
    
    def get_all_users(self):
        return User.query.all()