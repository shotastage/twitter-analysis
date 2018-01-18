# -*- encoding:utf-8 -*-
#
#   tweetgetter.py
#   tweetgetter
#
#   Copyright (c) 2018 Shota Shimazu. All rights reserved.
#

import sys
from tweetgetter.getflow import TweetGetFlow
from tweetgetter.agent import background_agent as ba

def main():
    args = sys.argv
    if len(args) == 1:
        print("""
Usage: tweetgetter
    -word "SEARCH WORD"
    -max  integer
    -as-agent=True or False
        """)

    # Remove own
    args.pop(0)


    # CLI Arguments
    search_word = args[1]
    search_word_num = args[3]

    if "True" in args[3]:
        launch_as_agent = True
    else:
        launch_as_agent = False


    # Flow instance
    flow = TweetGetFlow()


    if launch_as_agent:

        def wrap(search_word, search_word_num):
            flow.get_tweet(search_word, search_word_num)
        
        ba(wrap(search_word, search_word_num))
    else:
        flow.get_tweet(search_word, search_word_num)
