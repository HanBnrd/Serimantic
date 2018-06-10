# -*- coding: utf-8 -*-

"""
serimantic.nlp
~~~~~~~~~~~~~~~~~
This module implements the NLP functionalities of serimantic.

Created by Justinien Ghorra and Johann Benerradi on June 2018.

Copyright: (c) 2017-2018 by Justinien Ghorra and Johann Benerradi
License: GNU GPL 3.0, see LICENSE for more details
"""

import lib.tmdbsimple as tmdb

from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.tag import pos_tag

from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from collections import OrderedDict

class Processing:

    acceptedWordsFile = open('../data/acceptedWords.txt', 'r+', encoding='utf8')
    acceptedWords = []
    for word in acceptedWordsFile.read().splitlines():
        acceptedWords.append(word)

    stopWordsFile = open('../data/stopWords.txt','r+',encoding='utf8')
    customStopWords = []
    for word in stopWordsFile.readlines():
        customStopWords.append(word)


    def getOverviews(self, series):
        """
        Get overviews from series, seasons and episodes
        """
        numberOfSeasons = tmdb.TV(series['id']).info()['number_of_seasons']
        numberOfEpisodes = 0
        seasonOverviews = ""
        episodeOverviews = ""

        # Series
        seriesOverview = series['overview']

        # Seasons
        for seasonNumber in range(numberOfSeasons):
            seasonOverview = tmdb.TV_Seasons(series['id'],seasonNumber+1).info()['overview']
            seasonOverviews = seasonOverviews + " " + seasonOverview # from the raw seasons synopsis to the filtered ones

            # Episodes
            episodesPerSeason = len(tmdb.TV_Seasons(series['id'],seasonNumber+1).info()['episodes'])
            numberOfEpisodes = numberOfEpisodes + episodesPerSeason
            for episodeNumber in range(episodesPerSeason):
                episodeOverview = tmdb.TV_Episodes(series['id'],seasonNumber+1,episodeNumber+1).info()['overview']
                episodeOverviews = episodeOverviews + " " + episodeOverview
        overviews = seriesOverview + " " + seasonOverviews + " " + episodeOverviews
        return overviews


    def filter(self, text):
        """
        Remove stop words
        """
        stopWords = set(stopwords.words('english'))
        tokenizer = RegexpTokenizer(r'[\w-]+')
        words = tokenizer.tokenize(text)
        taggedWords = pos_tag(words) # determine the type of each word
        filteredWords = [word for word, pos in taggedWords if ((pos != 'NNP') and (pos != 'CD') and (pos != 'NNPS'))] # remove proper nouns and numerals
        finalFilteredWords = []
        for w in filteredWords:
            low_w = w.lower()
            if (low_w not in stopWords) and (low_w not in self.customStopWords): # keep only lower-case words which are not "stop words"
                finalFilteredWords.append(low_w)
        return finalFilteredWords


    def makeLexicalField(self, word, words_field, words_count):
        """
        Make lexical field
        """
        synsW = wordnet.synsets(word)
        if len(synsW) > 0:
            key = synsW[0].name().split('.')[0]
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


    def selectKeywords(self, words, supervised=False, top=20):
        """
        Get top keywords
        """
        words_field = {}
        words_count = {}
        finalWords = {}
        for w in words:
            self.makeLexicalField(w, words_field, words_count)

        arrKeys = list(words_field)
        for keyA in arrKeys:
            for keyB in arrKeys:
                if keyA != keyB and keyA in words_field[keyB]: # words match if they are linked by their field
                    words_count[keyA] = words_count[keyA] + 1
        ordDict = OrderedDict(sorted(words_count.items(), key=lambda k: k[1], reverse=True))
        ordKeys = list(ordDict.keys())
        finalWords = []

        # Supervised processing
        if supervised:
            i = 0
            while len(finalWords) < 20 and i < len(ordKeys):
                word = ordKeys[i]
                if word in self.acceptedWords:
                    finalWords.append(word)
                else:
                    answer = input('Is "' + word + '" a stop word ? [y/n] : ')
                    if(answer == 'y'):
                        self.customStopWords.append(word)
                        self.stopWordsFile.write(word + '\n')
                    else:
                        self.acceptedWords.append(word)
                        self.acceptedWordsFile.write(word + '\n')
                        finalWords.append(word)
                i = i+1
            return finalWords

        # Unsupervised processing
        else:
            if(len(ordDict) > top):
                for i in range (top):
                    word = ordKeys[i]
                    finalWords.append(word)
            return finalWords
