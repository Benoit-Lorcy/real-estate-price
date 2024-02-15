import pytest
from flask import Flask
from flask_jwt_extended import JWTManager
from main import app  # Import the Flask app instance from the main module

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'your_secret_key'
    JWTManager(app)
    return app  # Return the Flask app instance

@pytest.fixture
def client(app):
    return app.test_client()

def test_create_token(client):
    response = client.post('/api/v1/token', json={'username': 'admin', 'password': 'password'})
    assert response.status_code == 200
    assert 'access_token' in response.json

def test_create_token_invalid_credentials(client):
    response = client.post('/api/v1/token', json={'username': 'wrong_user', 'password': 'wrong_password'})
    assert response.status_code == 401
    assert 'msg' in response.json

def test_get_villes(client):
    response = client.get('/api/v1/villes/M')
    assert response.status_code == 200
    assert len(response.json) > 0

# def test_get_quartiers(client):
#     response = client.get('/api/v1/quartiers/paris')
#     assert response.status_code == 200
#     assert len(response.json) > 0

# def test_prices_ville_quartier_get(client):
#     response = client.get('/api/v1/prices/ville/paris/quartier/marais')
#     assert response.status_code == 200
#     assert 'Prix_au_m2' in response.json

# def test_prices_ville_quartier_get_not_found(client):
#     response = client.get('/api/v1/prices/ville/unknown/quartier/unknown')
#     assert response.status_code == 404
#     assert 'message' in response.json

# def test_prices_ville_quartier_put(client):
#     response = client.put('/api/v1/prices/ville/paris/quartier/marais', json={'Prix_au_m2': 10000})
#     assert response.status_code == 200
#     assert 'message' in response.json
