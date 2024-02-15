# real-estate-price

Un projet simple en Python, SQLite, HTML et JavaScript pour afficher le prix moyen de l'immobilier par ville et par quartier.


## Description

Ce project implémente :

- Une API REST
- Une base de données SQLite
- Un moyen d'authentification par clé
- Une interface utilisateur pour tester l'API
- Des tests unitaires


## Installation

Prérequis : Python doit être installé sur votre machine.

Clonez le dépôt :

```bash
git clone https://github.com/Benoit-Lorcy/real-estate-price
cd real-estate-price
```

Créez un environnement virtuel :
```bash
python -m venv venv
```

Activez l'environnement virtuel (sous Windows) :
```bash
.\venv\Scripts\Activate.ps1
```

Installez les dépendances requises :
```bash
pip install -r requirements.txt
```

Lancez l'application :
```bash
python main.py
```

Vous pouvez maintenant tester l'application !


## Utilisation

Accédez à l'interface utilisateur en ouvrant un navigateur web et en visitant l'URL : http://localhost:5000.

Utilisez l'interface pour tester les différents endpoints de l'API.


## Endpoints

`GET /` : Retourne index.html (l'interface utilisateur).\
`POST /api/v1/token` : Nécessite un nom d'utilisateur et un mot de passe au format JSON, et retourne access_token (jeton d'accès).\
`GET /api/v1/villes/<string:ville_filter>` : Retourne la liste des villes possibles en fonction du début du nom d'une ville.\
`GET /api/v1/quartiers/villes/<string:ville>` : Retourne la liste des quartiers d'une ville donnée.\
`GET /api/v1/prices/ville/<string:ville>/quartier/ <string:quartier>` : Retourne le prix moyen d'une ville et d'un quartier donnés.


## Importation des données

Pour importer les données à partir d'un fichier CSV dans la base de données, le script `import_data.py` fourni dans le projet est exécuté.


## Tests Unitaires

Le projet est accompagné de tests unitaires réalisés avec le framework Pytest.
Pour exécuter les tests unitaires, assurez-vous d'être dans le répertoire `real-estate-price` où se trouve le projet. Ensuite, utilisez la commande suivante :
```bash
pytest test_real_estate.py
```

## Auteurs

- Benoit Lorcy
- Cyann Piquet
