"""
Ce module permet l'écriture des mots clés dans le fichier default
"""

from enum import Enum
import lib.tmdbsimple as tmdb
import os

def writeDefaultFile (seriesName, keywords):
    with open("../data/default.tal", "a", encoding="utf8") as writeFile:
        stringToWrite = seriesName + "|"
        for k in keywords:
            stringToWrite = stringToWrite + k + ";"
        writeFile.write(stringToWrite + "\n")
    writeFile.close()
