"""
Main script to get a series recommendation
"""

import lib as sc # serimantic package


def main():
    print('Serimantic : add.py')
    print('*******************')

    # Display processed series
    manage = sc.Manage()
    TVShowList = manage.getProcessedSeries()
    print('Available series : ' + str(TVShowList))
    print('*******************')

    # Input series name
    TVShowInput = input('You liked : ')
    if TVShowInput not in TVShowList:
        print('Series not processed yet')

    else:
        bestSeries = manage.recommendation(TVShowInput)
        interSet = manage.intersection(TVShowInput, bestSeries)
        print('You may also like : ' + bestSeries)
        print('Common keywords : ' + str(interSet))


if __name__ == '__main__':
    main()
