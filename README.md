# Serimantic #

**Title:** Serimantic  
**Keywords:** NLP, recommendation, TV series  
**Version:** 2.0.2  
**Date:** April 2018  
**Authors:** Johann Benerradi, Rachel Confiant-Duté, Justinien Ghorra, Laurine Jeannot, Quentin Pouvreau  
**Web site:** [UFR Mathématiques et Informatique](http://mathinfo.univ-lorraine.fr)  
**Platform:** Python 3, Django  
**License:** GNU GPL 3.0  


Relies on [tmdbsimple](https://github.com/celiao/tmdbsimple) v1.7.0 modified to get keywords of TV series (stored in *src/lib*)  


**Description:**  
TV series recommendation based on keyword extraction through semantic analysis of overviews  


**Requires:**  
  - [Python 3](https://www.python.org/downloads/)  
  - [NLTK 3.2.5](http://www.nltk.org)  
  - [TMDB API key](https://www.themoviedb.org/documentation/api)  


### API key configuration
Run *src/keyConfig.py* with Python 3 and type in the key  


## Web interface
### Installation
#### 1) Install Django and Django Rest Framework with pip
```bash
sudo apt install python3-pip

sudo apt install python3-django

pip install django

pip install djangorestframework

pip install markdown   # Markdown support for the browsable API

pip install django-filter
```

#### 2) Install MySQL Server and the connector for Python
```bash
sudo apt install mysql-server

sudo apt install libmysqlclient-dev python-dev python-mysqldb

sudo apt install python3-mysql.connector

pip install mysqlclient
```

#### 3) Create a user to access a new database *serimantic* in MySQL
```bash
mysql -u root -p
```
```sql
CREATE DATABASE serimantic;

GRANT ALL PRIVILEGES on serimantic.* to ‘user’@’localhost’ IDENTIFIED BY ‘password’;

exit
```

#### 4) Fill in the SECRET_KEY in *Serimantic/settings.py*

#### 5) Migrate the database
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

##### You're good to go !


## Command-line interface
### Keyword Extraction on the basic corpus
Run *src/defaultMain.py* with Python 3 (keywords are stored in *data/nlpdata.txt*)  
Modify *data/defaultseries.txt* to extract keywords on a different series basis  
This process might have already been done  

### Adding a series to the corpus
Run *src/addSeries.py* with Python 3 and folow the instructions (new keywords are stored in *data/nlpdata.txt*)  

### Series recommendation
Run *src/recommendation.py* with Python 3 and folow the instructions  
A series close to that indicated will be recommended and the common keywords will be displayed  


*(c) Université de Lorraine - Nancy*
