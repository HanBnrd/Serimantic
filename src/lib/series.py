"""
Ce module permet d'obtenir la liste de séries déja analysées par des outils de TAL
"""

def getList(filereader):
    TVShowList = []
    for row in filereader:
        TVShowList.append(row.split('|')[0])
    filereader.seek(0)
    return TVShowList
