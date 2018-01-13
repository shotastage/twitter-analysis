# -*- encoding:utf-8 -*-
#
#   getflow.py
#   tweetgetter
#
#   Copyright (c) 2018 Shota Shimazu. All rights reserved.
#

from requests_oauthlib import OAuth1Session, OAuth1
from requests.exceptions import ConnectionError, ReadTimeout, SSLError
from tweetgetter import config
from tweetgetter import entries

import json
import requests
import urllib
import numpy
import sys
import io



class TweetGetFlow():
    
    def __init__(self):
        self._twitter = OAuth1(config.consumer_key, config.consumer_key_secret, config.access_token, config.access_token_secret)

        # Set default string enconding as UTF-8
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding = "utf-8")


    
    def get_tweet(self, search, count):

        print(search, count)

        entry_point = entries.TwitterAPIEntries.search
        params = {'q': search,
              'count':count,
        }

        req = self._make_req_url(search, count)
        res = requests.get(req, auth = self._twitter)
        data = res.json()['statuses']



        if req.status_code == 200: # On Sucess
            # 
            return "testing"
        else:                     # On failure
            print ("Error: %d" % req.status_code)
            return "testing"

    def _make_req_url(self, word, count):
        return entries.TwitterAPIEntries.search + "?count=" + count + "&lang=ja&q=" + word


    def _file_IO(self, data):
        pass
