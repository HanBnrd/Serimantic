# -*- coding: utf-8 -*-

"""
serimantic.series
~~~~~~~~~~~~~~~~~
This module implements the series management functionalies of serimantic.

Created by Justinien Ghorra and Johann Benerradi on June 2018.

:copyright: (c) 2017-2018 by Justinien Ghorra and Johann Benerradi
:license: GNU GPL 3.0, see LICENSE for more details
"""

import lib.tmdbsimple as tmdb

class Series()

    """
    Get the list of series that have already been processed
    """
    def getProcessedSeries(self, filereader):
        seriesList = []
        for row in filereader:
            seriesList.append(row.split('|')[0])
        filereader.seek(0)
        return seriesList


    """
    Get overviews keywords from series, seasons and episodes
    """
    # TODO : mettre traitement dans un main

    def getKeywords(self, series):
        numberOfSeasons = tmdb.TV(series['id']).info()['number_of_seasons']
        numberOfEpisodes = 0
        seasonsWords = []
        episodesWords = []

        # Series
        seriesWords = series['overview']

        # Seasons
        for seasonNumber in range(numberOfSeasons):
            seasonOverview = tmdb.TV_Seasons(series['id'],seasonNumber+1).info()['overview']
            seasonsWords.extend(seasonOverview) # from the raw seasons synopsis to the filtered ones

            # Episodes
            episodesPerSeason = len(tmdb.TV_Seasons(series['id'],seasonNumber+1).info()['episodes'])
            numberOfEpisodes = numberOfEpisodes + episodesPerSeason
            for episodeNumber in range(episodesPerSeason):
                episodeOverview = tmdb.TV_Episodes(series['id'],seasonNumber+1,episodeNumber+1).info()['overview']
                episodesWords.extend(episodeOverview)

        return seriesWords, seasonsWords, episodesWords
