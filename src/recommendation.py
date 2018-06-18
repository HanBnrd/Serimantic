"""
Recommandation d'une série à partir d'une autre
"""

from lib.series import getProcessedSeries

print('****************************')
print('| Recommandation de séries |')
print('****************************')
print('Liste de séries disponibles : ')
nlpdata = open('../data/nlpdata.txt','r',encoding='utf8')
TVShowList = getProcessedSeries(nlpdata) # Obtention de la liste de séries importées
print(TVShowList)
print('')
TVShowInput = input('Choisissez une série que vous avez aimé : ')
if TVShowInput not in TVShowList:
    print('Erreur : Série non disponible')
else:
    refList = []
    testList = []
    bestList = []
    bestTVShow = ''
    for row in nlpdata: # Récupération des mots clés de la série sélectionnée
        if row.split('|')[0] == TVShowInput:
            refList = row.split('|')[1].split(';')
            refList = refList[:len(refList)-1]
    nlpdata.seek(0)
    bestInter = 0
    for row in nlpdata: # Comparaison des mots clés de la série aux autres
        if row.split('|')[0] != TVShowInput:
            testList = row.split('|')[1].split(';')
            testInter = len(set(refList).intersection(set(testList)))
            if testInter > bestInter:
                bestTVShow = row.split('|')[0]
                bestList = testList
                bestInter = testInter
    interSet = set(refList).intersection(set(bestList))
    print('')
    print('Nous vous recommandons :')
    print(bestTVShow)
    print('Ressemblances : '+str(interSet))
