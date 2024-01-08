from flask import Flask, jsonify
import csv

app = Flask(__name__)

# Load CSV data into a dictionary
data = {}
with open('prix_immobilier_fictif.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        ville = row['Ville']
        if ville not in data:
            data[ville] = []
        data[ville].append({
            'Quartier': row['Quartier'],
            'Prix au m²': row['Prix au m²']
        })

# Endpoint to filter cities
@app.route('/villes/name/<string:filter>')
def get_cities(filter):
    filtered_villes = [ville for ville in data if ville.lower().startswith(filter.lower())]
    return jsonify(filtered_villes)

# Endpoint to get districts of the first matching city
@app.route('/villes/name/<string:filter>/quartiers')
def get_quartiers(filter):
    for ville, quartiers in data.items():
        if ville.lower().startswith(filter.lower()):
            unique_quartiers = set(q['Quartier'] for q in quartiers)
            return jsonify(list(unique_quartiers))
    return jsonify([])

# Endpoint to get the price of a specific district in a city
@app.route('/villes/name/<string:filter>/quartiers/<string:quartier>/price')
def get_price(filter, quartier):
    for ville, quartiers in data.items():
        if ville.lower().startswith(filter.lower()):
            for q in quartiers:
                if q['Quartier'].lower() == quartier.lower():
                    return jsonify(q['Prix au m²'])
    return jsonify("Not Found")

if __name__ == '__main__':
    app.run(debug=True)