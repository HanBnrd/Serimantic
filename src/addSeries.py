"""
Main script to add series keywords to data
"""

import lib.tmdbsimple as tmdb
import lib as sc # serimantic package


def process(searchResult, supervised):
    print("Processing, please wait...")
    nlp = sc.Processing()
    text = nlp.getOverviews(searchResult)
    words = nlp.filter(text)
    keywords = nlp.selectKeywords(words, supervised=supervised)
    return keywords


def main():
    # API key config
    APIkey = open('../api.key','r',encoding='utf8')
    tmdb.API_KEY = APIkey.readline().split('\n')[0]
    APIkey.close()

    # Input series name
    seriesName = input("Series name :\n")

    # Search
    search = tmdb.Search()
    search.tv(query=seriesName)
    if (len(search.results) > 0):
        result = search.results[0] # take the first result

        # Check name
        TVShowName = result['original_name']
        correctName = input('Do you mean '+ TVShowName + ' ? [y/n]\n')
        if correctName is not 'y':
            print("Canceled")
        else:
            # Check if not already processed
            manage = sc.Manage()
            TVShowList = manage.getProcessedSeries()
            if TVShowName in TVShowList:
                print('Error : Series already processed')
            else:
                # Decide whether supervised or not
                supervisedInput = input('Supervised processing ? [y/n]\n')
                if supervisedInput is 'y':
                    supervised = True
                else:
                    supervised = False

                # Process
                keywords = process(result, supervised)

                # Write in file
                manage.writeSeriesKeywords(TVShowName, keywords)
                print("Done")


if __name__ == '__main__':
    main()
