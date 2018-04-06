"""
Recommendation for API
"""

def recommendation(series):
    default = open('data/default.tal','r',encoding='utf8')
    refList = []
    testList = []
    bestList = []
    bestSeries = ''
    for row in default: # get keywords from series
        if row.split('|')[0] == series:
            refList = row.split('|')[1].split(';')
            refList = refList[:len(refList)-1]
    default.seek(0)
    bestInter = 0
    for row in default: # comparing keywords to other series
        if row.split('|')[0] != series:
            testList = row.split('|')[1].split(';')
            testInter = len(set(refList).intersection(set(testList)))
            if testInter > bestInter:
                bestSeries = row.split('|')[0]
                bestList = testList
                bestInter = testInter
    return bestSeries
