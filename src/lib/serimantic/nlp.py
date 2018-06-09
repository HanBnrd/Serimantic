# -*- coding: utf-8 -*-

"""
serimantic.nlp
~~~~~~~~~~~~~~~~~
This module implements the NLP functionality of serimantic.

Created by Justinien Ghorra and Johann Benerradi on June 2018.

:copyright: (c) 2017-2018 by Justinien Ghorra and Johann Benerradi
:license: GNU GPL 3.0, see LICENSE for more details
"""

"""
filter
"""

from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.tag import pos_tag

stopWordsFile = open('../data/stopWords.txt','r',encoding="utf8")
stopWords = []
for word in stopWordsFile.readlines():
    stopWords.append(word)
stopWordsFile.close()

def filter (text):
    stopWords = set(stopwords.words("english"))
    tokenizer = RegexpTokenizer(r'[\w-]+')
    customStopWords = ["premiered", "created", "produced","contains", "season", "episode", "episodes", "airing", "association"]
    words = tokenizer.tokenize(text)
    tagged_words = pos_tag(words) # determine the type of each word
    filtered_words = [word for word,pos in tagged_words if ((pos != 'NNP') and (pos != 'CD') and (pos != 'NNPS'))] # push out proper nouns and numerals
    final_filtered_words = []
    for w in filtered_words:
        low_w = w.lower()
        if (low_w not in stopWords) and (low_w not in customStopWords): # keep only lower-case words which are not "stop words"
            final_filtered_words.append(low_w)
    return final_filtered_words


"""
semantic
"""
"""
Ce module permet l'analyse sémantique du corpus par l'utilisation des synonymes
"""

from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
from collections import OrderedDict

def makeLexicalField(word, words_field, words_count, stopWords):
    synsW = wn.synsets(word)
    if len(synsW) > 0:
        key = synsW[0].name().split(".")[0]
        if key not in stopWords:
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
    with open("../data/stopWords.txt", "r+", encoding="utf8") as stopWordsFile:
        stopWords = []
        for word in stopWordsFile.read().splitlines():
            stopWords.append(word)
        words_field = {}
        words_count = {}
        finalWords = {}
        for w in motsSerie:
            makeLexicalField(w, words_field, words_count, stopWords)
        for w in motsSaisons:
            makeLexicalField(w, words_field, words_count, stopWords)
        for w in motsEpisodes:
            makeLexicalField(w, words_field, words_count, stopWords)

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
    stopWordsFile.close()
    return finalWords

def selectVerifiedKeywords(motsSerie, motsSaisons, motsEpisodes):
    with open("../data/acceptedWords.txt", "r+", encoding="utf8") as acceptedWordsFile:
        acceptedWords = []
        for word in acceptedWordsFile.read().splitlines():
            acceptedWords.append(word)
        with open("../data/stopWords.txt", "r+", encoding="utf8") as stopWordsFile:
            stopWords = []
            for word in stopWordsFile.read().splitlines():
                stopWords.append(word)
            words_field = {}
            words_count = {}
            finalWords = {}
            for w in motsSerie:
                makeLexicalField(w, words_field, words_count, stopWords)
            for w in motsSaisons:
                makeLexicalField(w, words_field, words_count, stopWords)
            for w in motsEpisodes:
                makeLexicalField(w, words_field, words_count, stopWords)

            arrKeys = list(words_field)
            for keyA in arrKeys:
                for keyB in arrKeys:
                    if keyA != keyB and keyA in words_field[keyB]: # words match if they are linked by their field
                        words_count[keyA] = words_count[keyA] + 1
            ordDict = OrderedDict(sorted(words_count.items(), key=lambda k: k[1], reverse=True))
            ordKeys = list(ordDict.keys())
            finalWords = []
            i = 0
            while len(finalWords) < 20 and i < len(ordKeys):
                word = ordKeys[i]
                if word not in stopWords:
                    if word in acceptedWords:
                        finalWords.append(word)
                    else:
                        txtInput = "\"" + word + "\" est-il est un stopWord ? (y/n) : "
                        answer = input(txtInput)
                        if(answer == 'y'):
                            stopWords.append(word)
                            stopWordsFile.write(word + "\n")
                        else:
                            acceptedWords.append(word)
                            acceptedWordsFile.write(word + "\n")
                            finalWords.append(word)
                i = i+1
        stopWordsFile.close()
    acceptedWordsFile.close()
    return finalWords
