#!/usr/bin/env python3
from google import search
import sys

def get_site_restriction(filename):
    sites = []
    with open(filename, 'r') as infile:
        for line in infile:
            sites.append('site:{}'.format(line.replace('\n', '')))
    assert len(sites) > 0, 'The file {} is empty'.format(filename)
    return '({})'.format(' OR '.join(sites))

def main(args):
    siteRestriction = get_site_restriction('academic_articles.txt')
    for url in search('"Elon Musk" ' + siteRestriction, stop=10):
        print(url)
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
