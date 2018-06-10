"""
Add series keywords for the default series
"""
# DEPRECATED : TODO

import lib.tmdbsimple as tmdb
import lib as sc # serimantic package

def main():
    APIkey = open('../api.key', 'r', encoding='utf8')
    key = APIkey.readline().split('\n')[0]
    APIkey.close()
    tmdb.API_KEY = key # database key
    search = tmdb.Search() # searching instantiation

    defaultseries = open('../data/defaultseries.txt', 'r', encoding='utf8')

    for line in defaultseries.readlines():

        search.tv(query=line)
        if (len(search.results) > 0):
            s = search.results[0] # take the first result
            print(s['original_name'])
            getKeywords(s)

    defaultseries.close()
