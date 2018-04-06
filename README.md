# Serimantic #

Title: Serimantic  
Keywords: NLP, recommendation, TV series  
Version: 1.0.0  
Date: dec 2017  
Authors: Justinien Ghorra, Laurine Jeannot, Johann Benerradi, Rachel Confiant-Duté  
Web site: <http://mathinfo.univ-lorraine.fr>  
Platform: Python 3  
License: GNU GPL 3.0  

Use of [tmdbsimple](https://github.com/celiao/tmdbsimple) v1.7.0, modified to get keywords of TV series (stored in src/lib)

Description:  
TV series recommendation based on keyword extraction through semantic analysis of overviews  


Requires:  
  - [Python 3.x](https://www.python.org/download/releases/3.0/)  
  - [NLTK 3.2.5](http://www.nltk.org)  
  - [TMDB API key](https://www.themoviedb.org/documentation/api)  

## Web part
### Installation
#### 1) Install Django and Django Rest Framework
```bash    
pip install django

pip install djangorestframework

pip install markdown       # Markdown support for the browsable API.

pip install django-filter

```
#### 2) Install MySQL Server and the connector for Python
```bash
sudo apt install mysql-server

sudo apt install libmysqlclient-dev python-dev python-mysqldb

sudo apt install python3-mysql.connector 

pip install mysqlclient

```
#### 3) In MySQL, create a new database "serimantic"
```bash

mysql -u root -p

create database serimantic;

exit
```
#### 4) Put your own settings.py file into Serimantic/ folder (a template will be located in the project)

#### 5) Make database migration
```bash

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py loaddata data/fixtures/initData.json

```
#### 6) Create a superuser account for the database 
```bash

python3 manage.py createsuperuser

```
#### 7) Run the server
```bash

python3 manage.py runserver

```
#### 8) Everything is (normally) done !

### Utilisation
##### Configuration de l'API key  
Lancer keyConfig.py avec Python3 et saisir la clé

##### Extraction des mots clés des séries de base  
Lancer defaultMain.py avec Python 3 (les mots clés sont enregistrés dans samples/saves/default.tal)  
Pour extraire les mots clés avec une base de séries différente, modifier le fichier samples/tvlist.txt  
Selon la version de Serimantic, ce traitement est déjà réalisé bien qu'il soit possible de le refaire en cas de problème  

##### Ajout d'une série au corpus  
Lancer addSerie.py avec Python 3 et suivre les intructions en console  
Les mots clés sont enregistrés dans samples/saves/default.tal  

##### Recommandation de série  
Lancer recommendation.py avec Python3 et suivre les instructions en console  
Une série proche de celle indiquée sera recommandée et les mots clés en communs affichés  


*(c) Université de Lorraine - Nancy*
