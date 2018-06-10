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
        Write series name and keywords in files
        """
        default = open("../data/default.tal", "a", encoding="utf8")
        line = seriesName + "|"
        for word in keywords:
            line = line + word + ";"
        default.write(line + "\n")
        default.close()
        tvlist = open('../data/tvlist.txt','a',encoding='utf8')
        tvlist.write(seriesName + "\n")
        tvlist.close()
