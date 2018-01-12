import requests

from requests_oauthlib import OAuth1Session
from requests.exceptions import ConnectionError, ReadTimeout, SSLError
import json
import config
import numpy as np


url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
params = {'screen_name':'@shota_mixtr',
          'exclude_replies':True,
          'include_rts':False,
          'count':200}



class TweetGetFlow():
    
    def __init__(self,connection, db, twdata, meta):
        self._twitter       = OAuth1Session(config.consumer_key, config.consumer_key_secret, config.access_token, config.access_token_secret)
        self._connection    = connection
        self._db            = db
        self._twdata        = twdata
        self._meta          = meta 

    
    def get_tweet(self):
        pass
