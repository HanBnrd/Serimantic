# Needs to be executed in the Serimantic folder, using python3 -m data.convertIntoFixturesWithTmdb.py

from src.lib import tmdbsimple as tmdb

names = '['
namesIndex = 1
keywords = '['
keywordsIndex = 1
relation = '['
relationIndex = 1

fichier = open('data/nlpdata.txt','r',encoding="utf8")

keywordsVisited = []

APIkey = open('api.key','r',encoding="utf8")
key = APIkey.readline().split("\n")[0]
APIkey.close()

tmdb.API_KEY = key # database key
search = tmdb.Search() # searching instantiation

for line in fichier.readlines():
	splitted = line.split("|")
	seriesName = splitted[0]

	search.tv(query=seriesName)

	s = search.results[0] # take the first result
	idTmdb = s['id']

	names = names + '\n	{\n		"model": "api.name",\n		"pk": '+ str(namesIndex)+',\n		"fields": {\n			"name" : "' + splitted[0] + '", \n			"tmdb_id" : "' + str(idTmdb) + '" \n		}\n	},'
	
	words = splitted[1].split(";")
	for key in words:
		if(key != "\n"):
			if(key not in keywordsVisited):
				keywords = keywords + '\n	{\n		"model": "api.keyword",\n		"pk": '+ str(keywordsIndex)+',\n		"fields": {\n			"keyword" : "' + key + '" \n		}\n	},'
				relation = relation +  '\n	{\n		"model": "api.tag",\n		"pk": '+ str(relationIndex)+',\n		"fields": {\n			"name_id" : ' + str(namesIndex) + ', \n			"keyword_id" : ' + str(keywordsIndex) + '\n		}\n	},'
				keywordsVisited.append(key)
				keywordsIndex = keywordsIndex + 1
			else:
				relation = relation +  '\n	{\n		"model": "api.tag",\n		"pk": '+ str(relationIndex)+',\n		"fields": {\n			"name_id" : ' + str(namesIndex) + ', \n			"keyword_id" : ' + str(keywordsVisited.index(key)+1) + '\n		}\n	},'				
			relationIndex = relationIndex + 1
	namesIndex = namesIndex + 1

fichier.close()
names = names + '\n]'
keywords = keywords + '\n]'
relation = relation + '\n]'

with open("data/fixtures/names.json", "w", encoding="utf8") as writeFile:
	writeFile.write(names)
	writeFile.close()

with open("data/fixtures/words.json", "w", encoding="utf8") as writeFile:
	writeFile.write(keywords)
	writeFile.close()	

with open("data/fixtures/tags.json", "w", encoding="utf8") as writeFile:
	writeFile.write(relation)
	writeFile.close()

print("WARNING : after the execution, we need to manually delete the last comma of the .json created")