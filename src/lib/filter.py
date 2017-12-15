"""
Ce module permet de filtrer un texte de manière à ne conserver que les mots les
plus utiles à la catégorisation d'une série
"""

from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.tag import pos_tag

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
