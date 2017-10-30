from .search import search

def collect(*args, stop=10):
    '''
    Collect data focused on a particular topic
    '''
    urls = search(*args, stop=stop, restrictFile='data/articles.txt')
    return urls
