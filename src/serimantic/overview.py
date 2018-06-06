"""
Ce module permet d'obtenir les résumés des séries, saisons et épisodes et de les
traiter avec les modules filter puis semantic
"""

import lib.tmdbsimple as tmdb
import lib.filter as fil
import lib.semantic as sem
from lib.writer import writeDefaultFile

def addInList(series, verify=False):
    seriesWords = fil.filter(series['overview']) # from the raw series synopsis to the filtered one
    numberOfSeasons = tmdb.TV(series['id']).info()['number_of_seasons']
    numberOfEpisodes = 0
    seasonsWords = []
    episodesWords = []
    for seasonNumber in range(numberOfSeasons):
        seasonOverview = tmdb.TV_Seasons(series['id'],seasonNumber+1).info()['overview']
        seasonsWords.extend(fil.filter(seasonOverview)) # from the raw seasons synopsis to the filtered ones

        episodesPerSeason = len(tmdb.TV_Seasons(series['id'],seasonNumber+1).info()['episodes'])
        numberOfEpisodes = numberOfEpisodes + episodesPerSeason
        for episodeNumber in range(episodesPerSeason):
            episodeOverview = tmdb.TV_Episodes(series['id'],seasonNumber+1,episodeNumber+1).info()['overview']
            episodesWords.extend(fil.filter(episodeOverview)) # from the raw episodes synopsis to the filtered ones

    if verify:
        keywords = sem.selectVerifiedKeywords(seriesWords, seasonsWords, episodesWords)
    else:
        keywords = sem.selectKeywords(seriesWords, seasonsWords, episodesWords)
    writeDefaultFile(series['original_name'], keywords)
