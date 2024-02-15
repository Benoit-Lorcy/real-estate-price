# real-estate-price

A simple project in Python and JavaScript

## Description

Ce projet Python implémente une API REST respectant les principes CRUD (Create, Read, Update, Delete). L'objectif est de créer une API à partir d'un fichier CSV contenant des données sur les villes, les quartiers et les prix immobiliers associés. L'API offre trois endpoints principaux :

1. `/api/v1/villes` : Affiche toutes les villes.
2. `/api/v1/quartiers/villes/<nom_ville>` : Affiche tous les quartiers d'une ville spécifique.
3. `/api/v1/price/quartiers/<nom_quartier>/villes/<nom_ville>` : Affiche le prix spécifique à un quartier d'une ville donnée.

Le projet respecte la méthode REST en utilisant les différentes méthodes HTTP (GET dans ce cas) pour effectuer des opérations sur les ressources. De plus, il suit les principes CRUD en permettant la récupération (Read) des données.

## Installation

1. Clonez le dépôt : `git clone  https://github.com/Benoit-Lorcy/real-estate-price`
2. Installez les dépendances : `pip install Flask==2.0.1` `pip install flask_jwt_extended` `pip install flask_cors`

## Importation des données

Pour importer les données à partir d'un fichier CSV dans la base de données, exécutez le script `import_data.py` fourni dans le projet.

## Utilisation

1. Exécutez l'application : `python main.py`
2. Accédez à l'API via votre navigateur via `localhost:5000` ou un outil de requêtage comme [Postman](https://www.postman.com/).

## Tests Unitaires
Le projet est accompagné de tests unitaires réalisés avec le framework Pytest. 
Pour exécuter les tests, utilisez la commande suivante :
`pytest test_real_estate.py`

## Endpoint

- **GET /api/v1/villes** : Affiche la ville donnée.
- **GET /api/v1/quartiers/<nom_ville>** : Affiche les quartiers dans une ville donnée.
- **GET /api/v1/prices/ville/<nom_ville>/quartier/<nom_quartier>** : Affiche les prix d'un quartier spécifique dans une ville donnée.

## Exemple d'utilisation

- Pour obtenir les différents villes commençant par la lettre "M" : `localhost:5000/villes/m`
- Pour obtenir les différents quartiers à Paris : `localhost:5000/quartiers/villes/paris`
- Pour obtenir le prix du quartier Sud à Tokyo : `localhost:5000/price/quartiers/sud/villes/tokyo`

## Auteurs

- Benoit Lorcy
- Cyann Piquet

## Licence
/