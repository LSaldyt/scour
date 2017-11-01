#!/usr/bin/env python3
import os.path

from google import search as google_search

from .tag import Tag

dirname  = os.path.dirname(os.path.realpath(__file__))
datapath = dirname + '/../data/'

def get_site_restriction(filename):
    '''
    Get a site-restriction argument for google search
    '''
    sites = []
    with open(filename, 'r') as infile:
        for line in infile:
            sites.append('site:{}'.format(line.replace('\n', '')))
    assert len(sites) > 0, 'The file {} is empty'.format(filename)
    return '({})'.format(' OR '.join(sites))

def search(*args, stop=10, restrictFiles=None):
    '''
    Perform a google search using *args
    '''
    if restrictFiles is not None and len(restrictFiles) > 0:
        restrictions = []
        for filename in restrictFiles:
            path = datapath + filename
            restrictions += get_site_restriction(path)
        args += ('({})'.format(' | '.join(restrictions)),)
    urls = []
    for url in google_search(' '.join(args), stop=stop):
        urls.append(url)
    return urls
