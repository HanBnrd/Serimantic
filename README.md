# Serimantic #

**Title:** Serimantic  
**Keywords:** NLP, recommendation, TV series  
**Version:** 2.0.0  
**Date:** april 2018  
**Authors:** Johann Benerradi, Rachel Confiant-Duté, Justinien Ghorra, Laurine Jeannot, Quentin Pouvreau  
**Web site:** [UFR Mathématiques et Informatique](http://mathinfo.univ-lorraine.fr)  
**Platform:** Python 3, Django  
**License:** GNU GPL 3.0  


**Description:**  
TV series recommendation based on keyword extraction through semantic analysis of overviews  


## Web part
### Installation
#### 1) Install Django and Django Rest Framework with pip
```bash
sudo apt install python-pip

sudo apt install python3-django

pip install django

pip install djangorestframework

pip install markdown   # Markdown support for the browsable API.

pip install django-filter

```
#### 2) Install MySQL Server and the connector for Python
```bash
sudo apt install mysql-server

sudo apt install libmysqlclient-dev python-dev python-mysqldb

sudo apt install python3-mysql.connector 

pip install mysqlclient

```
#### 3) In MySQL, create a user to access a new database "serimantic"
```bash
mysql -u root -p

CREATE DATABASE serimantic;

GRANT ALL PRIVILEGES on serimantic.* to ‘user’@’localhost’ IDENTIFIED BY ‘password’;

exit

```
#### 4) Put your own settings.py file into Serimantic/ folder (a template will be located in the project)

#### 5) Make database migration
```bash
python3 manage.py migrate

python3 manage.py loaddata data/fixtures/initData.json

```
#### 6) [Optional] Create a superuser to access the database as admin in Django 
```bash
python3 manage.py createsuperuser

```
#### 7) Run the server
```bash
python3 manage.py runserver

```
### You're good to go !


## The NLP engine  
Use of [tmdbsimple](https://github.com/celiao/tmdbsimple) v1.7.0, modified to get keywords of TV series (stored in src/lib)  


**Requires:**  
  - [Python 3.x](https://www.python.org/download/releases/3.0/)  
  - [NLTK 3.2.5](http://www.nltk.org)  
  - [TMDB API key](https://www.themoviedb.org/documentation/api)  


#### Configuration de l'API key  
Lancer keyConfig.py avec Python 3 et saisir la clé

#### Extraction des mots clés des séries de base  
Lancer defaultMain.py avec Python 3 (les mots clés sont enregistrés dans samples/saves/default.tal)  
Pour extraire les mots clés avec une base de séries différente, modifier le fichier samples/tvlist.txt  
Selon la version de Serimantic, ce traitement est déjà réalisé bien qu'il soit possible de le refaire en cas de problème  

#### Ajout d'une série au corpus  
Lancer addSerie.py avec Python 3 et suivre les intructions en console  
Les mots clés sont enregistrés dans samples/saves/default.tal  

#### Recommandation de série  
Lancer recommendation.py avec Python 3 et suivre les instructions en console  
Une série proche de celle indiquée sera recommandée et les mots clés en communs affichés  


*(c) Université de Lorraine - Nancy*
