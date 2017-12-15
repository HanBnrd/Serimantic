"""
Création du corpus à partir des mots clés des séries de la liste de base
"""

import lib.tmdbsimple as tmdb
from lib.writer import writeDefaultFile
from lib.overview import addInList

APIkey = open('../api.key','r',encoding="utf8")
key = APIkey.readline().split("\n")[0]
APIkey.close()
tmdb.API_KEY = key # database key
search = tmdb.Search() # searching instantiation

fichier = open('../samples/tvlist.txt','r',encoding="utf8")

index = -1
for line in fichier.readlines():
    index = index + 1
    search.tv(query=line)
    if (len(search.results) > 0):
        s = search.results[0] # take the first result
        print(s['original_name'])
        addInList(s)
