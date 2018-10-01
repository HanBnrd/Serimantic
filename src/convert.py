"""
Convert data into fixtures
"""

import lib.tmdbsimple as tmdb


def main():
    # Set API key
    APIkey = open('../api.key','r',encoding='utf8')
    tmdb.API_KEY = APIkey.readline()
    APIkey.close()

    # Open the data file
    nlpdata = open('../data/nlpdata.txt','r',encoding="utf8")

    # Initialize lists
    names = '['
    namesIndex = 1
    keywords = '['
    keywordsIndex = 1
    relation = '['
    relationIndex = 1
    keywordsVisited = []

    search = tmdb.Search() # searching instantiation
    for line in nlpdata.readlines():
        seriesName = line.split("|")[0]
        wordList = line.split("|")[1].split(";")

        search.tv(query=seriesName)
        idTmdb = search.results[0]['id'] # take the first result

        names = names + '\n	{\n		"model": "api.name",\n		"pk": ' + str(namesIndex) + ',\n		"fields": {\n			"name" : "' + seriesName + '", \n			"tmdb_id" : "' + str(idTmdb) + '" \n		}\n	},'
        for word in wordList:
            if(word != "\n"):
                if(word not in keywordsVisited):
                    keywords = keywords + '\n	{\n		"model": "api.keyword",\n		"pk": ' + str(keywordsIndex) + ',\n		"fields": {\n			"keyword" : "' + word + '" \n		}\n	},'
                    relation = relation +  '\n	{\n		"model": "api.tag",\n		"pk": ' + str(relationIndex) + ',\n		"fields": {\n			"name_id" : ' + str(namesIndex) + ', \n			"keyword_id" : ' + str(keywordsIndex) + '\n		}\n	},'
                    keywordsVisited.append(word)
                    keywordsIndex = keywordsIndex + 1
                else:
                    relation = relation +  '\n	{\n		"model": "api.tag",\n		"pk": ' + str(relationIndex) + ',\n		"fields": {\n			"name_id" : ' + str(namesIndex) + ', \n			"keyword_id" : ' + str(keywordsVisited.index(word)+1) + '\n		}\n	},'				
                relationIndex = relationIndex + 1
        namesIndex = namesIndex + 1

    nlpdata.close()
    names = names + '\n]'
    keywords = keywords + '\n]'
    relation = relation + '\n]'

    with open("data/fixtures/names.json", "w", encoding="utf8") as writeFile:
        writeFile.write(names)
        writeFile.close()

    with open("data/fixtures/keywords.json", "w", encoding="utf8") as writeFile:
        writeFile.write(keywords)
        writeFile.close()	

    with open("data/fixtures/tags.json", "w", encoding="utf8") as writeFile:
        writeFile.write(relation)
        writeFile.close()

    print("WARNING : please delete manually the last comma of the .json created")


if __name__ == '__main__':
    main()
