# -*- coding: utf-8 -*-

"""
serimantic.manage
~~~~~~~~~~~~~~~~~
This module implements the file management functionalities of serimantic.

Created by Justinien Ghorra and Johann Benerradi on June 2018.

Copyright: (c) 2017-2018 by Justinien Ghorra and Johann Benerradi
License: GNU GPL 3.0, see LICENSE for more details
"""

class Manage():

    filereader = open('../data/nlpdata.txt','r',encoding='utf8')
    filewriter = open('../data/nlpdata.txt', 'a', encoding='utf8')

    def getProcessedSeries(self):
        """
        Get the list of series that have already been processed
        """
        seriesList = []
        for row in self.filereader:
            seriesList.append(row.split('|')[0])
        self.filereader.seek(0)
        return seriesList


    def recommendation(self, series):
        """
        Get the closest series
        """
        refList = []
        testList = []
        bestList = []
        bestSeries = ''
        bestInter = 0

        # Get keywords from the series
        for row in self.filereader:
            if row.split('|')[0] == series:
                refList = row.split('|')[1].split(';')
                refList = refList[:len(refList)-1]
        self.filereader.seek(0)

        # Compare keywords to other series
        for row in self.filereader:
            if row.split('|')[0] != series:
                testList = row.split('|')[1].split(';')
                testInter = len(set(refList).intersection(set(testList)))
                if testInter > bestInter:
                    bestSeries = row.split('|')[0]
                    bestList = testList
                    bestInter = testInter
        self.filereader.seek(0)

        return bestSeries


    def intersection(self, seriesA, seriesB):
        """
        Get the common keywords of two series
        """
        keywordsA = []
        keywordsB = []

        for row in self.filereader:
            # Get keywords of seriesA
            if row.split('|')[0] == seriesA:
                keywordsA = row.split('|')[1].split(';')
                keywordsA = keywordsA[:len(keywordsA)-1]

            # Get keywords of seriesB
            if row.split('|')[0] == seriesB:
                keywordsB = row.split('|')[1].split(';')
                keywordsB = keywordsB[:len(keywordsB)-1]
        self.filereader.seek(0)

        # Get intersection
        interSet = set(keywordsA).intersection(set(keywordsB))

        return interSet


    def writeSeriesKeywords(self, seriesName, keywords):
        """
        Write series name and keywords in file
        """
        line = seriesName + '|'
        for word in keywords:
            line = line + word + ';'
        self.filewriter.write(line + '\n')
