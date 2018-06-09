# -*- coding: utf-8 -*-

"""
serimantic.series
~~~~~~~~~~~~~~~~~
This module implements the series management functionalies of serimantic.

Created by Justinien Ghorra and Johann Benerradi on June 2018.

:copyright: (c) 2017-2018 by Justinien Ghorra and Johann Benerradi
:license: GNU GPL 3.0, see LICENSE for more details
"""

import tmdbsimple as tmdb

class Series:

    def getProcessedSeries(self, filereader):
        """
        Get the list of series that have already been processed
        """
        seriesList = []
        for row in filereader:
            seriesList.append(row.split('|')[0])
        filereader.seek(0)
        return seriesList


    def getKeywords(self, series):
        """
        Get overviews keywords from series, seasons and episodes
        """
        # TODO : mettre traitement dans un main
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
