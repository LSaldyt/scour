#!/usr/bin/env python3
from google import search as google_search

from .tag import Tag

def search(*args, stop=10):
    urls = []
    for url in google_search(' '.join(args), stop=stop):
        urls.append(url)
    return urls
