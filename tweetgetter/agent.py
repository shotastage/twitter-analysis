# -*- encoding:utf-8 -*-
#
#   agent.py
#   tweetgetter
#
#   Copyright (c) 2018 Shota Shimazu. All rights reserved.
#

from time import sleep

def background_agent(func):
    while True:
        # Avoid Twitter API request regulation
        sleep(1)
        func()
