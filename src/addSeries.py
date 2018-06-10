"""
Add series keywords to data
"""

import lib.tmdbsimple as tmdb
import lib as sc # serimantic package

def main():
    APIkey = open('../api.key','r',encoding="utf8")
    key = APIkey.readline().split("\n")[0]
    APIkey.close()
    tmdb.API_KEY = key # database key
    search = tmdb.Search() # searching instantiation

    seriesName = input("Series name :\n")
    search.tv(query=seriesName)
    if (len(search.results) > 0):
        s = search.results[0] # take the first result
        TVShowName = s['original_name']
        default = open('../data/default.tal','r',encoding='utf8')
        series = sc.Series()
        TVShowList = series.getProcessedSeries(default)
        default.close()
        correctName = input('Do you mean '+ TVShowName + ' ? [y/n]\n')
        if correctName is not 'y':
            print("Canceled")
        else:
            if TVShowName in TVShowList:
                print('Error : Series already processed')
            else:
                supervised = input('Supervised processing ? [y/n]\n')
                print("Processing, please wait...")
                text = series.getOverviews(s)
                nlp = sc.Processing()
                words = nlp.filter(text)

                # Unsupervised processing
                if supervised is not 'y':
                    keywords = nlp.selectKeywords(words)
                    writer = sc.Writer()
                    writer.writeSeriesKeywords(TVShowName, keywords)
                    print("Done")

                # Supervised processing
                else:
                    keywords = nlp.selectKeywords(words, supervised=True)
                    writer = sc.Writer()
                    writer.writeSeriesKeywords(TVShowName, keywords)
                    print("Done")

if __name__ == '__main__':
    main()
