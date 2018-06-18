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


    def writeSeriesKeywords(self, seriesName, keywords):
        """
        Write series name and keywords in file
        """
        line = seriesName + '|'
        for word in keywords:
            line = line + word + ';'
        self.filewriter.write(line + '\n')
