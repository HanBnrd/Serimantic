# -*- coding: utf-8 -*-

"""
serimantic.writer
~~~~~~~~~~~~~~~~~
This module implements the file management functionality of serimantic.

Created by Justinien Ghorra and Johann Benerradi on June 2018.

:copyright: (c) 2017-2018 by Justinien Ghorra and Johann Benerradi
:license: GNU GPL 3.0, see LICENSE for more details
"""

class Writer():

    def writeSeriesKeywords(slef, seriesName, keywords):
        """
        Write series name and keywords in file
        """
        nlpdata = open('../data/nlpdata.txt', 'a', encoding='utf8')
        line = seriesName + '|'
        for word in keywords:
            line = line + word + ';'
        nlpdata.write(line + '\n')
        nlpdata.close()
