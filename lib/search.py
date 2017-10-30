#!/usr/bin/env python3
from google import search as google_search

from .tag import Tag

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

def search(*args, stop=10, restrictFile=None):
    '''
    Perform a google search using *args
    '''
    if restrictFile is not None:
        args += (get_site_restriction(restrictFile),)
    urls = []
    for url in google_search(' '.join(args), stop=stop):
        urls.append(url)
    return urls
