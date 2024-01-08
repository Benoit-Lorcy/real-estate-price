# real-estate-price
A simple project in python and htmx

# Nom du Projet

Projet API de Prix Immobilier

## Description

Ce projet Python vous permet de créer une API à partir d'un fichier CSV contenant des données sur les villes, les quartiers et les prix immobiliers associés. L'API offre trois endpoints principaux :

1. `/villes` : Affiche toutes les villes disponibles.
2. `/ville/quartiers` : Affiche tous les quartiers d'une ville spécifique.
3. `/ville/quartier` : Affiche les prix d'un quartier dans une ville donnée.

## Installation

1. Clonez le dépôt : `git clone https://github.com/votre-utilisateur/votre-projet.git`
2. Installez les dépendances : `pip install -r requirements.txt`

## Configuration

1. Ajoutez votre fichier CSV de données dans le répertoire du projet.

## Utilisation

1. Exécutez l'application : `python app.py`
2. Accédez à l'API via votre navigateur ou un outil de requêtage comme [curl](https://curl.se/) ou [Postman](https://www.postman.com/).

## Endpoints

- **GET /villes** : Affiche toutes les villes disponibles.
- **GET /ville/quartiers** : Affiche tous les quartiers d'une ville spécifique. Utilisez `/ville/quartiers?nom_ville=NOM_DE_LA_VILLE`.
- **GET /ville/quartier** : Affiche les prix d'un quartier dans une ville donnée. Utilisez `/ville/quartier?nom_ville=NOM_DE_LA_VILLE&nom_quartier=NOM_DU_QUARTIER`.

## Exemple d'utilisation

- Pour obtenir toutes les villes : `localhost:5000/villes`
- Pour obtenir tous les quartiers d'une ville : `localhost:5000/ville/quartiers?nom_ville=NOM_DE_LA_VILLE`
- Pour obtenir les prix d'un quartier d'une ville : `localhost:5000/ville/quartier?nom_ville=NOM_DE_LA_VILLE&nom_quartier=NOM_DU_QUARTIER`

## Auteurs

- Benoit Lorcy <votre@email.com>
- Cyann Piquet

## Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.
