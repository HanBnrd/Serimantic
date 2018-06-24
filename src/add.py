"""
Main script to add keywords from a series to the data.
"""

import lib.tmdbsimple as tmdb
import lib as sc # serimantic package


def process(searchResult, supervised):
    print('Processing ' + searchResult['original_name'] + '...')
    nlp = sc.Processing()
    text = nlp.getOverviews(searchResult)
    words = nlp.filter(text)
    keywords = nlp.selectKeywords(words, supervised=supervised)
    return keywords


def main():
    print('Serimantic : add.py')
    print('*******************')

    # Set API key
    APIkey = open('../api.key','r',encoding='utf8')
    tmdb.API_KEY = APIkey.readline()
    APIkey.close()

    # Input series name
    seriesName = input('Series name : ')

    # Search
    search = tmdb.Search()
    search.tv(query=seriesName)
    if (len(search.results) > 0):
        result = search.results[0] # take the first result

        # Check name
        TVShowName = result['original_name']
        correctName = input('Do you mean '+ TVShowName + ' ? [y/n] ')
        if correctName is not 'y':
            print('Canceled')
        else:
            # Check if not already processed
            manage = sc.Manage()
            TVShowList = manage.getProcessedSeries()
            if TVShowName in TVShowList:
                print(TVShowName + ' already processed')
            else:
                # Decide whether supervised or not
                supervisedInput = input('Supervised processing ? [y/n] ')
                if supervisedInput is 'y':
                    supervised = True
                else:
                    supervised = False

                # Process
                keywords = process(result, supervised)

                # Write in file
                manage.writeSeriesKeywords(TVShowName, keywords)
                print('Done')


if __name__ == '__main__':
    main()
