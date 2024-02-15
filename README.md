# real-estate-price

Un project simple en python, sqlite, html et javascript pour afficher le prix moyen par ville et par quartier

## Description

Ce project implémente :

- Une api rest
- Une base sqlite
- Un moyen d'authentification par clé
- Un front pour tester l'api
- Des tests

## Installation

Requirements : il faut avoir python d'installé

```bash
git clone https://github.com/Benoit-Lorcy/real-estate-price
cd real-estate-price
python -m venv venv
./venv/Scripts/Activate.ps1
pip install -r requirements.txt
python main.py
```

Now you can try the application !

## Endpoints

`GET /` : Returns index.html (the front end) \
`POST /api/v1/token` : Needs an username and a password in json, returns access_token \
`GET /api/v1/villes/<string:ville_filter>` : retoune la liste de ville possible à partir du début du nom d'une ville\
`GET /api/v1/quartiers/villes/<string:ville>` : retourne la list de quartiers d'une ville\
`GET /api/v1/prices/ville/<string:ville>/quartier/ <string:quartier>` : retourne le prix donné une ville et un quartier

## Importation des données

Pour importer les données à partir d'un fichier CSV dans la base de données, exécutez le script `import_data.py` fourni dans le projet.

## Tests Unitaires

Le projet est accompagné de tests unitaires réalisés avec le framework Pytest.
Pour exécuter les tests, utilisez la commande suivante :
`pytest test_real_estate.py`

## Auteurs

- Benoit Lorcy
- Cyann Piquet
