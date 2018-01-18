# -*- encoding:utf-8 -*-
#
#   getflow.py
#   tweetgetter
#
#   Copyright (c) 2018 Shota Shimazu. All rights reserved.
#

from tweetgetter import config
from tweetgetter import entries
from tweetgetter.savecsv import save_as_csv as sac

from requests_oauthlib import OAuth1Session
import csv
import json
import sys, codecs
import pandas as pd


class TweetGetFlow():
    
    def __init__(self):
        self._twitter = OAuth1Session(
            config.consumer_key,
            config.consumer_key_secret,
            config.access_token,
            config.access_token_secret
        )

        self._url = "https://api.twitter.com/1.1/search/tweets.json?"

    
    def get_tweet(self, search, count):
        params = {
            "q": str(search),
            "lang": "ja",
            "result_type": "recent",
            "count": count
        }
        req = self._twitter.get(self._url, params = params)
        tweets = json.loads(req.text)

        save_list = []

        for tweet in tweets["statuses"]:
            tmp_list = [tweet["user"]["screen_name"],
                        tweet["user"]["name"], 
                        tweet["text"]]
            
            save_list.append(tmp_list)

        df = pd.DataFrame(save_list,
                    columns = ["id", "name", "text"],
            )
 
        df.to_csv("tweets.csv",encoding="utf-8")



    def _make_req_url(self, word, count):
        return "https://api.twitter.com/1.1/search/tweets.json" + "?count=" + count + "&lang=ja&q=" + word


    def _log_tweets(self, data):

        csv_list = []


        for tweet in data:
            print("----------------------------------------------------------------------------------------------------")
            ##print(tweet["id"])
            ##print(tweet["created_at"])
            print(tweet["text"])

            print("6371263712361283618")
            type(tweet["text"])
            
            errr = json.load(tweet)
            print(errr)
            #csv_list.append(text)


        self._file_IO(csv_list)    

    def _file_IO(self, data):
        
        sac("tweets.csv", data)
