# -*- coding: utf-8 -*-


import sys
from tweetgetter.getflow import TweetGetFlow


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

    search_word = args[1]
    search_word_num = args[2]

    flow = TweetGetFlow()
    flow.get_tweet(search_word, search_word_num)
