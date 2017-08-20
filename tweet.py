import json
import pymongo
import tweepy


# Variables that contains the user credentials to access Twitter API
access_key = "161075524-Te53YeIMJTE3FFcRao36FDWNHpfKNMCdQxgC1qqi"
access_secret = "qWKY661B3HqJ9Aw4aXYrKSaO2OcEHUHS8YYisRdFcqUEu"
consumer_key = "jHWxqeGUc3Od5qE1m0VEBmwuQ"
consumer_secret = "UCvxpXDcZnpjA5r8Kv6Guyiinz4HkSpYxfOwP7Qk9uv977P8Mj"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


class CustomStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        super(tweepy.StreamListener, self).__init__()
        self.db = pymongo.MongoClient().tweets

    def on_data(self, tweet):
        print(json.loads(tweet)['text'])
        print(str(self.db.nintendo.count()) + " tweets accumulated")
        print("Size is: "
              + str(self.db.command("dbstats")['dataSize'])
              #+ str(self.db.command("collstats","nintendo")['size'])
              + " bytes")
        self.db.nintendo.insert(json.loads(tweet))


    def on_error(self, status_code):
        return True  # Don't kill the stream

    def on_timeout(self):
        return True  # Don't kill the stream


for x in range(1, 1000):
    try:
        sapi = tweepy.streaming.Stream(auth, CustomStreamListener(api))
        sapi.filter(track=['nintendo']) #change this
    except Exception as e:
        print ('retrying')
