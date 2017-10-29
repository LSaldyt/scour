#!/usr/bin/env python3
import argparse
import sys
import pickle

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

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("subcommand", type=str,
                        help="Select a subcommand of scour to run")
    parser.add_argument('subargs', type=str, nargs='*',
                        help='Sub arguments fed into a sub command')
    args = parser.parse_args()

    try:
        with open('.project.pkl', 'rb') as infile:
            project = pickle.load(infile)
    except:
        project = Project()

    project_command = getattr(project, args.subcommand)
    project_command(*args.subargs)

    with open('.project.pkl', 'wb') as outfile:
        pickle.dump(project, outfile)

    return 0

if __name__ == '__main__':
    sys.exit(main())
