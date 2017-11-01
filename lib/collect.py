from .search import search
from .result import Result

import os.path

dirname  = os.path.dirname(os.path.realpath(__file__))
datapath = dirname + '/../data/'

def collect(*args, stop=10):
    '''
    Collect data focused on a particular topic
    '''
    print(args)
    urls = search(*args, stop=stop, restrictFile=datapath + 'articles')
    return Result(args, urls)
