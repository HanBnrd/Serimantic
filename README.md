# Serimantic #

Title: Serimantic  
Keywords: recommendation, series, NLP  
Version: 1.0  
Date: dec 2017  
Authors: Justinien Ghorra, Laurine Jeannot, Johann Benerradi, Rachel Confiant-Duté  
Web site: <http://mathinfo.univ-lorraine.fr>  
Platform: Python 3  
License: GNU GPL 3.0  

Use of [tmdbsimple](https://github.com/celiao/tmdbsimple) v1.7.0, modified to get keywords of TV series (stored in src/lib)


Description:  
Recommandation de série basée sur des mots clés obtenus par  l'analyse sémantique des synopsis des séries, saisons, et épisodes  


Requis:  
  1) [Python 3.0](https://www.python.org/download/releases/3.0/)  
  2) [NLTK 3.2.5](http://www.nltk.org)  
  3) [TMDB API key](https://www.themoviedb.org/documentation/api) (à ajouter dans un fichier api.key à la racine)


Utilisation:  
  1) Extraction des mots clés des séries de base  
Lancer defaultMain.py avec Python 3 (les mots clés sont enregistrés dans samples/saves/default.tal)  
Pour extraire les mots clés avec une base de séries différente, modifier le fichier samples/tvlist.txt  
Selon la version de Serimantic, ce traitement est déjà réalisé bien qu'il soit possible de le refaire en cas de problème  

  2) Ajout d'une série au corpus  
Lancer addSerie.py avec Python 3 et suivre les intructions en console (les mots clés sont enregistrés dans samples/saves/default.tal)  
Selon la version de Serimantic, le traitement pour certaines séries en plus de celles initiales peut avoir été réalisé dans le fichier samples/saves/default.tal  

  3) Recommandation de série  
Lancer recommendation.py avec Python3 et suivre les instruction en console  
Une série proche de celle indiquée sera recommandée et les mots clés en communs affichés  


Pour plus d'information voir le rapport de projet  


(c) Université de Lorraine - Nancy
