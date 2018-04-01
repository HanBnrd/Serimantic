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
