import requests

from requests_oauthlib import OAuth1Session
from requests.exceptions import ConnectionError, ReadTimeout, SSLError

import numpy as np

import json
import datetime

import config
import entries

url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
params = {'screen_name':'@shota_mixtr',
          'exclude_replies':True,
          'include_rts':False,
          'count':200}



class TweetGetFlow():
    
    def __init__(self):
        self._twitter       = OAuth1Session(config.consumer_key, config.consumer_key_secret, config.access_token, config.access_token_secret)

    
    def get_tweet(self, search, count):
        entry_point = entries.TwitterAPIEntries.search
        params = {'q': search,
              'count':count,
        }

        req = self._twitter.get(url, params = params)

        if req.status_code == 200: # On Sucess
            # 
            return "testing"
        else:                     # On failure
            print ("Error: %d" % req.status_code)
            return "testing"


flow = TweetGetFlow()

print(str(flow.get_tweet("Twitter", 1000)))
