# -*- coding: utf-8 -*-

"""
serimantic.nlp
~~~~~~~~~~~~~~~~~
This module implements the NLP functionalities of serimantic.

Created by Justinien Ghorra and Johann Benerradi on June 2018.

:copyright: (c) 2017-2018 by Justinien Ghorra and Johann Benerradi
:license: GNU GPL 3.0, see LICENSE for more details
"""

from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.tag import pos_tag

from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from collections import OrderedDict

class Processing:

    def __init__():
        self.acceptedWordsFile = open("../data/acceptedWords.txt", "r+", encoding="utf8")
        self.acceptedWords = []
        for word in acceptedWordsFile.read().splitlines():
            self.acceptedWords.append(word)

        self.stopWordsFile = open('../data/stopWords.txt','r',encoding="utf8")
        self.stopWords = []
        for word in stopWordsFile.readlines():
            self.stopWords.append(word)

        self.customStopWords = ["premiered", "created", "produced","contains", "season", "episode", "episodes", "airing", "association"]


    def filter(self, text):
        """
        Remove stop words
        """
        self.stopWords = set(stopwords.words("english"))
        tokenizer = RegexpTokenizer(r'[\w-]+')
        words = tokenizer.tokenize(text)
        taggedWords = pos_tag(words) # determine the type of each word
        filteredWords = [word for word, pos in tagged_words if ((pos != 'NNP') and (pos != 'CD') and (pos != 'NNPS'))] # remove proper nouns and numerals
        finalFilteredWords = []
        for w in filteredWords:
            low_w = w.lower()
            if (low_w not in self.stopWords) and (low_w not in self.customStopWords): # keep only lower-case words which are not "stop words"
                finalFilteredWords.append(low_w)
        return finalFilteredWords


    def makeLexicalField(self, word, words_field, words_count):
        """
        Make lexical field
        """
        # TODO : pourquoi pas de return ?
        synsW = wordnet.synsets(word)
        if len(synsW) > 0:
            key = synsW[0].name().split(".")[0]
            if key not in self.stopWords:
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


    def selectKeywords(self, words, top=20):
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
        if(len(ordDict) > top):
            for i in range (top):
                word = ordKeys[i]
                finalWords.append(word)
        return finalWords

    def selectVerifiedKeywords(self, words, top=20):
        """
        Get top keywords (supervised)
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
        i = 0
        while len(finalWords) < 20 and i < len(ordKeys):
            word = ordKeys[i]
            if word not in self.stopWords:
                if word in self.acceptedWords:
                    finalWords.append(word)
                else:
                    txtInput = "Is \"" + word + "\" a stopWord ? (y/n) : "
                    answer = input(txtInput)
                    if(answer == 'y'):
                        self.stopWords.append(word)
                        self.stopWordsFile.write(word + "\n")
                    else:
                        self.acceptedWords.append(word)
                        self.acceptedWordsFile.write(word + "\n")
                        finalWords.append(word)
            i = i+1
        return finalWords
