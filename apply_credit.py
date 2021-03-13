#!/usr/bin/env python3.8
"""Insert author metadata based on a mysql dump of author information."""
import csv
import pprint

def load_author_info():
    """Tokenize the author info."""
    with open('author-info.txt') as fhandle:
        posts = csv.reader(fhandle, delimiter='\t')
        for post in posts:
            pprint.pprint(post)

def main():
    """Main"""
    print("hey")
    load_author_info()

if __name__ == "__main__":
    main()
