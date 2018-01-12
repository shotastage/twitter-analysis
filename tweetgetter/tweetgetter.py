# -*- coding: utf-8 -*-


import sys

def main():
    args = sys.argv
    if len(args) == 1:
        print("""
Usage: tweetgetter
    -word "SEARCH WORD"
    -max  integer
        """)

    # Remove own
    args.pop(0)
