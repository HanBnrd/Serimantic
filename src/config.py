"""
API key configuration
"""

def main():
    print('Serimantic : config.py')
    print('**********************')

    key = input('TMDB API key : ')
    apikey = open('../api.key','w',encoding='utf8')
    apikey.write(key)
    apikey.close()
    print('Done')


if __name__ == '__main__':
    main()
