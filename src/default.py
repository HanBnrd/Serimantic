"""
Main script to add keywords from default series to the data.
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
    print('Serimantic : default.py')
    print('***********************')

    # Set API key
    APIkey = open('../api.key','r',encoding='utf8')
    tmdb.API_KEY = APIkey.readline()
    APIkey.close()

    # Decide whether supervised or not
    supervisedInput = input('Supervised processing ? [y/n] ')
    if supervisedInput is 'y':
        supervised = True
    else:
        supervised = False

    # Open the default series file
    defaultseries = open('../data/defaultseries.txt', 'r', encoding='utf8')

    search = tmdb.Search() # searching instantiation
    for line in defaultseries.readlines():
        search.tv(query=line)
        if (len(search.results) > 0):
            result = search.results[0] # take the first result
            TVShowName = result['original_name']
            manage = sc.Manage()
            TVShowList = manage.getProcessedSeries()
            if TVShowName in TVShowList:
                print(TVShowName + ' already processed')
            else:
                # Process
                keywords = process(result, supervised)
                # Write in file
                manage.writeSeriesKeywords(TVShowName, keywords)

    # Close the default series file
    defaultseries.close()
    print('Done')


if __name__ == '__main__':
    main()
