"""
Ajout des mots clés d'une série dans le corpus
"""

import lib.tmdbsimple as tmdb
from lib.series import getProcessedSeries
from lib.overview import getKeywords

APIkey = open('../api.key','r',encoding="utf8")
key = APIkey.readline().split("\n")[0]
APIkey.close()
tmdb.API_KEY = key # database key
search = tmdb.Search() # searching instantiation

seriesName = input("Entrez un nom de série :\n")
search.tv(query=seriesName)
if (len(search.results) > 0):
    s = search.results[0] # take the first result
    TVShowName = s['original_name']
    default = open('../data/default.tal','r',encoding='utf8')
    TVShowList = getProcessedSeries(default)
    correctName = input('La série est-elle "'+ TVShowName + '" ? (y | n)\n')
    if (correctName == "y") :
        if TVShowName in TVShowList:
            print('Erreur : La série est déjà présente !')
        else:
            print("Ajout de la série, veuillez patienter...")
            getKeywords(s, True)
            tvlist = open('../data/tvlist.txt','a',encoding='utf8')
            tvlist.write(TVShowName+"\n")
            print("Série ajoutée !")
