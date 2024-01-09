from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
import sqlite3

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'your_secret_key' 
jwt = JWTManager(app)

def get_db_connection():
    conn = sqlite3.connect('data/real_estate_data.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/api/v1/token', methods=['POST'])
def create_token():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    # Validate username and password
    # For demo, it's hardcoded. In practice, verify with database or other secure system.
    if username != 'admin' or password != 'password':
        return jsonify({"msg": "Bad username or password"}), 401

    # Create JWT token
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)


@app.route('/api/v1/villes/<string:ville_filter>', methods=['GET'])
@jwt_required()
def get_villes(ville_filter):
    conn = get_db_connection()
    cursor = conn.cursor()
    # Adjust the query to match ville names that start with the filter string
    cursor.execute('SELECT DISTINCT Ville FROM real_estate WHERE Ville LIKE ?', (f'{ville_filter}%',))
    villes = cursor.fetchall()
    conn.close()

    return jsonify([ville['Ville'] for ville in villes])


@app.route('/api/v1/quartiers/<string:ville>', methods=['GET'])
@jwt_required()
def get_quartiers(ville):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT DISTINCT Quartier FROM real_estate WHERE Ville = ?', (ville,))
    quartiers = cursor.fetchall()
    conn.close()

    return jsonify([quartier['Quartier'] for quartier in quartiers])


@app.route('/api/v1/prices/ville/<string:ville>/quartier/<string:quartier>', methods=['GET', 'PUT'])
@jwt_required()
def prices_ville_quartier(ville, quartier):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute('SELECT Prix_au_m2 FROM real_estate WHERE Ville = ? AND Quartier = ?', (ville, quartier))
        price = cursor.fetchone()
        conn.close()
        if price:
            return jsonify(price['Prix_au_m2'])
        else:
            return {'message': 'No data found'}, 404

    elif request.method == 'PUT':
        update_data = request.json
        cursor.execute('UPDATE real_estate SET Prix_au_m2 = ? WHERE Ville = ? AND Quartier = ?', 
                       (update_data['Prix_au_m2'], ville, quartier))
        conn.commit()
        conn.close()
        return {'message': 'Price updated'}

if __name__ == '__main__':
    app.run(debug=True)
