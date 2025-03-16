import pytest

from app import create_app
from app.db.database import db
from app.models.user import User
from app.config import TestConfig

app = create_app()


@pytest.fixture
def client():
    # Create a test client
    app = create_app()
    app.config.from_object(TestConfig)

    # Set up the database
    with app.app_context():
        db.create_all()

    yield app.test_client()

    # Tear down the database
    with app.app_context():
        db.drop_all()


def test_delete_user(client):
    with app.app_context():
        user = User(name="John Doe", email="johndoe@example.com")
        db.session.add(user)
        db.session.commit()

        response = client.delete(f'/users/{user.id}')
        assert response.status_code == 200

        # check, if user deleted
        db.session.refresh(user)
        assert user not in db.session
        user_after_deletion = User.query.first()
        assert user_after_deletion is None


def test_get_all_users(client):
    client.post('/users', json={'name': 'John Doe', 'email': 'johndoe@example.com'})
    response = client.get('/users')

    assert response.status_code == 200
    data = response.get_json()
    assert len(data) > 0


def test_get_user_by_id(client):
    with app.app_context():
        client.post('/users', json={'name': 'John Doe', 'email': 'johndoe@example.com'})
        user = User.query.first()
        assert user is not None


def test_update_user(client):
    with app.app_context():
        client.post('/users', json={'name': 'John Doe', 'email': 'johndoe@example.com'})
        user = User.query.first()
        user.name = 'Jane Doe'
        db.session.commit()
        updated_user = User.query.first()
        assert updated_user.name == 'Jane Doe'


def test_delete_user(client):
    with app.app_context():
        # create user, before delete
        user = User(name="John Doe", email="johndoe@example.com")
        db.session.add(user)
        db.session.commit()

        # check, if user exists in DB
        user_from_db = User.query.first()
        print(f"USERR {user_from_db}")
        print(f"USERR ID {user_from_db.id}")
        user_id = user_from_db.id
        print(f"user_id {user_id}")

        # delete user
        response = client.delete(f'/users/{user_id}')
        assert response.status_code == 200

        db.session.commit()

        # check if deleted
        user_after_deletion = User.query.get(user_id)
        assert user_after_deletion is None