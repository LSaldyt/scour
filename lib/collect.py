from .search import search
from .result import Result

import os.path

def fix_arg(arg):
    reserved = ['~', '-', '+', 'AND', 'OR', '&', '|']
    if ' ' in arg and all(r not in arg for r in reserved):
        arg = '"{}"'.format(arg)
    return arg

def separate_restrictors(args):
    searchArgs = []
    restrictors = []
    for arg in args:
        if arg.startswith('@'):
            restrictors.append(arg[1:])
        else:
            searchArgs.append(fix_arg(arg))
    return searchArgs, restrictors

def collect(*args, stop=10):
    '''
    Collect data focused on a particular topic
    '''
    #print(args)
    args, restrictors = separate_restrictors(args)
    #print(args)
    #print(restrictors)
    filterURLs = True
    urls = search(*args, stop=stop, restrictFiles=restrictors)
    filtered = []
    if filterURLs:
        for url in urls:
            keep = input('Keep {}?'.format(url)).lower() == 'y'
            if keep:
                filtered.append(url)
    return Result(args, filtered)
