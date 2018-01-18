# -*- encoding:utf-8 -*-
#
#   entries.py
#   tweetgetter
#
#   Copyright (c) 2018 Shota Shimazu. All rights reserved.
#

import enum

class TwitterAPIEntries(enum.Enum):
    search = 'https://api.twitter.com/1.1/search/tweets.json'
