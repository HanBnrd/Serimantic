"""
Functions for the Django API
"""

def recommendation(series):
    """
    Get the closest series
    """
    filereader = open('./data/nlpdata.txt','r',encoding='utf8')
    refList = []
    testList = []
    bestList = []
    bestSeries = ''
    bestInter = 0

    # Get keywords from the series
    for row in filereader:
        if row.split('|')[0] == series:
            refList = row.split('|')[1].split(';')
            refList = refList[:len(refList)-1]
    filereader.seek(0)

    # Compare keywords to other series
    for row in filereader:
        if row.split('|')[0] != series:
            testList = row.split('|')[1].split(';')
            testInter = len(set(refList).intersection(set(testList)))
            if testInter > bestInter:
                bestSeries = row.split('|')[0]
                bestList = testList
                bestInter = testInter
    filereader.seek(0)

    return bestSeries
