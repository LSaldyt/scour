#!/usr/bin/env python3
import sys

from project import Project

'''
Copied usage notes

i.e.

Using scour to build notes on renewable energy generation and storage

scour begin thesis

scour begin generation
scour collect "~renewable energy" ~generation --articles
...
scour end generation

scour sub storage
scour collect ~"renewable energy" ~"energy storage" --articles
...
scour end storage

scour end thesis

def get_site_restriction(filename):
    sites = []
    with open(filename, 'r') as infile:
        for line in infile:
            sites.append('site:{}'.format(line.replace('\n', '')))
    assert len(sites) > 0, 'The file {} is empty'.format(filename)
    return '({})'.format(' OR '.join(sites))
'''

def main(args):
    project = Project()
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
