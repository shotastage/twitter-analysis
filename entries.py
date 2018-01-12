import enum

@enum.Enum
class TwitterAPIEntries(enum.Enum):
    url = 'https://api.twitter.com/1.1/search/tweets.json'

    def entry(self):
        return "https://api.twitter.com/1.1/search/tweets.json"
