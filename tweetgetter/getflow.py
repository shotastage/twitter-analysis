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
import numpy as np
import re


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
            tmp_list = [
                    tweet["user"]["screen_name"],
                    tweet["user"]["name"],
                    self._format_text(tweet["text"])
            ]
            

            # Log text
            print("----------------------------------------------------------------------------------------------------")
            print(tweet["text"])


            save_list.append(tmp_list)

        df = pd.DataFrame(
            save_list,
            columns = ["id", "name", "text"],
        )
 
        df.to_csv("./tweets/" + str(np.random.rand()) + "tweets.csv", encoding="utf-8")



    def _log_tweets(self, data):

        csv_list = []


        for tweet in data:
            print("----------------------------------------------------------------------------------------------------")
            print(tweet["text"])
            type(tweet["text"])
            
            errr = json.load(tweet)
            print(errr)

    
    def _format_text(self, text):
 
        text=re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", text) # Remove URL
        text=re.sub('RT', "", text) # Remove RT
        text=re.sub('お気に入り', "", text) # Remove favo
        text=re.sub('まとめ', "", text) # Remove matome site
        text=re.sub(r'[!-~]', "", text) #半角記号,数字,英字
        text=re.sub(r'[︰-＠]', "", text) #全角記号
        text=re.sub('\n', " ", text) #改行文字
 
        return text
