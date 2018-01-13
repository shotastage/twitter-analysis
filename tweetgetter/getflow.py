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

        print("ワード" + search + "に対して" + count + "件のツイート取得を開始します。")

        req = self._make_req_url(search, count)
        res = requests.get(req, auth = self._twitter)
        data = res.json()['statuses']


        self._log_tweets(data)


    def _make_req_url(self, word, count):
        return "https://api.twitter.com/1.1/search/tweets.json" + "?count=" + count + "&lang=ja&q=" + word


    def _log_tweets(self, data):
        for tweet in data:
            print("----------------------------------------------------------------------------------------------------")
            print(tweet["id"])
            print(tweet["created_at"])
            print(tweet["text"])
    

    def _file_IO(self, data):
        pass
