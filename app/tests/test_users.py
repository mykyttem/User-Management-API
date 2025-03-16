import pytest

from app.app import create_app
from app.db.database import db, DATABASE_URL
from app.models.user import User


@pytest.fixture
def client():
    # Create a test client
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL

    # Set up the database
    with app.app_context():
        db.create_all()

    yield app.test_client()

    # Tear down the database
    with app.app_context():
        db.drop_all()


def test_create_user(client):
    response = client.post('/users/', json={'name': 'John Doe', 'email': 'johndoe@example.com'})
    assert response.status_code == 201
    data = response.get_json()

    assert data['name'] == 'John Doe'
    assert data['email'] == 'johndoe@gmail.com'


def test_get_all_users(client):
    client.post('/users/', json={'name': 'John Doe', 'email': 'johndoe@example.com'})
    response = client.get('/users/')

    assert response.status_code == 200
    data = response.get_json()
    assert len(data) > 0


def test_get_user_by_id(client):
    client.post('/users/', json={'name': 'John Doe', 'email': 'johndoe@example.com'})
    user = User.query.first()
    response = client.get(f'/users/{user.id}')
    assert response.status_code == 200
    data = response.get_json()

    assert data['id'] == user.id
    assert data['name'] == 'John Doe'
    assert data['email'] == 'johndoe@example.com'


def test_update_user(client):
    client.post('/users/', json={'name': 'John Doe', 'email': 'johndoe@example.com'})
    user = User.query.first()
    response = client.put(f'/users/{user.id}', json={'name': 'John Updated', 'email': 'johnupdated@example.com'})
    assert response.status_code == 200
    data = response.get_json()

    assert data['name'] == 'John Updated'
    assert data['email'] == 'johnupdated@example.com'


def test_delete_user(client):
    client.post('/users/', json={'name': 'John Doe', 'email': 'johndoe@example.com'})
    user = User.query.first()
    response = client.delete(f'/users/{user.id}')

    assert response.status_code == 200
    assert response.get_json()['message'] == 'User deleted successfully'

    user_after_delete = User.query.get(user.id)
    assert user_after_delete is None