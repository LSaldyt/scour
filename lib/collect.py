from .search import search

import os.path

dirname = os.path.dirname(os.path.realpath(__file__))
path    = dirname + '/../data/'

def collect(*args, stop=10):
    '''
    Collect data focused on a particular topic
    '''
    print(args)
    urls = search(*args, stop=stop, restrictFile=path + 'articles.txt')
    return urls
