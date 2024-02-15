import pytest
from flask import Flask
from flask_jwt_extended import JWTManager
from main import app  # Import the Flask app instance from the main module

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
        
@pytest.fixture
def auth_token(client):
    response = client.post('/api/v1/token', json={'username': 'admin', 'password': 'password'})
    token = response.get_json()['access_token']
    return token

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200

def test_create_token(client):
    response = client.post('/api/v1/token', json={'username': 'admin', 'password': 'password'})
    assert response.status_code == 200
    assert 'access_token' in response.json
    
def test_get_villes(client, auth_token):
    response = client.get('/api/v1/villes/M', headers={'Authorization': f'Bearer {auth_token}'})
    assert response.status_code == 200
    assert len(response.json) > 0

def test_get_quartiers(client, auth_token):
    response = client.get('/api/v1/quartiers/villes/Madrid', headers={'Authorization': f'Bearer {auth_token}'})
    assert response.status_code == 200
    assert len(response.json) > 0
    
def test_prices_ville_quartier(client, auth_token):
    response = client.get('/api/v1/prices/ville/Madrid/quartier/Ouest', headers={'Authorization': f'Bearer {auth_token}'})
    assert response.status_code == 200
    