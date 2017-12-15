"""
Ce module permet l'analyse sémantique du corpus par l'utilisation des synonymes
"""

from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
from collections import OrderedDict

def isInStopWords(word):
    stopWords = ["television", "series", "season", "start", "end", "return", "first", "interim", "aid", "learn", "brand", "bring", "decide", "go", "get", "new", "think", "give", "attempt", "discovery"]
    return word in stopWords

def makeLexicalField(word, words_field, words_count):
    synsW = wn.synsets(word)
    if len(synsW) > 0:
        key = synsW[0].name().split(".")[0]
        if not isInStopWords(key):
            if key not in words_field:
                words_field[key] = []
                words_count[key] = 1
            else:
                words_count[key] = words_count[key] + 1
            for syn in synsW:
                synWord = syn.name().split(".")[0]
                if(synWord != key and synWord not in words_field[key]): # add the synonyms
                    words_field[key].append(synWord)
                for lemma in syn.lemmas():
                    for per in lemma.pertainyms():
                        if per.name() not in words_field[key]: # add the pertainyms
                            words_field[key].append(per.name())
                    for rel in lemma.derivationally_related_forms():
                        if rel.name() not in words_field[key]: # add the related forms
                            words_field[key].append(rel.name())

def selectKeywords(motsSerie, motsSaisons, motsEpisodes):
    words_field = {}
    words_count = {}
    finalWords = {}
    for w in motsSerie:
        makeLexicalField(w, words_field, words_count)
    for w in motsSaisons:
        makeLexicalField(w, words_field, words_count)
    for w in motsEpisodes:
        makeLexicalField(w, words_field, words_count)

    arrKeys = list(words_field)
    for keyA in arrKeys:
        for keyB in arrKeys:
            if keyA != keyB and keyA in words_field[keyB]: # words match if they are linked by their field
                words_count[keyA] = words_count[keyA] + 1
    ordDict = OrderedDict(sorted(words_count.items(), key=lambda k: k[1], reverse=True))
    ordKeys = list(ordDict.keys())
    finalWords = []
    if(len(ordDict) > 20):
        for i in range (20):
            word = ordKeys[i]
            finalWords.append(word)
    return finalWords
