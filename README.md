# real-estate-price
A simple project in Python and JavaScript

# Nom du Projet

Projet API de Prix Immobilier

## Description

Ce projet Python vous permet de créer une API à partir d'un fichier CSV contenant des données sur les villes, les quartiers et les prix immobiliers associés. L'API offre trois endpoints principaux :

1. `/villes/name/<nom_ville>` : Affiche le nom d'une ville donnée.
1. `/villes/name/<nom_ville>/quartiers` : Affiche tous les quartiers d'une ville spécifique.
2. `/villes/name/<nom_ville>/quartiers/<nom_quartier>/price` : Affiche le prix spécifique à un quartier d'une ville donnée.

## Installation

1. Clonez le dépôt : `git clone  https://github.com/Benoit-Lorcy/real-estate-price`
2. Installez les dépendances : `pip install Flask==2.0.1`

## Utilisation

1. Exécutez l'application : `python main.py`
2. Accédez à l'API via votre navigateur via `localhost:5000` ou un outil de requêtage comme [Postman](https://www.postman.com/).

## Endpoint

- **GET /villes/name/<nom_ville>** : Affiche la ville donnée.
- **GET /villes/name/<nom_ville>/quartiers** : Affiche les quartiers dans une ville donnée.
- **GET /villes/name/<nom_ville>/quartiers/<nom_quartier>/price** : Affiche les prix d'un quartier spécifique dans une ville donnée.

## Exemple d'utilisation

- Pour obtenir les différents villes commençant par la lettre "M" : `localhost:5000/villes/name/m`
- Pour obtenir les différents quartiers à Paris : `localhost:5000/villes/name/tokyo/quartiers`
- Pour obtenir le prix d'un quartier spécifique à Tokyo : `localhost:5000/villes/name/tokyo/quartiers/sud/price`

## Auteurs

- Benoit Lorcy
- Cyann Piquet

## Licence
/
