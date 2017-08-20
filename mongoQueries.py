import json
import pymongo
import datetime
import time

db = pymongo.MongoClient().tweets
def TweetsPerHour():
    count = db.nintendo.count()
    distinctDays = 5 * 24 #Average hours
    average = count/distinctDays
    return average

def TweetPercentWithWord(word):
    count = db.nintendo.count()
    relatedToWord = db.nintendo.find({'text': {'$regex': word, '$options': 'i'}}).count()
    return relatedToWord/count

def TweetsDistinctLocation():
    locations = db.nintendo.distinct("location")
    return len(locations)

#For converting the strings for twitter dates to datetime (takes too much resources)
#for doc in db.nintendo.find():
#    doc['created_at'] = datetime.datetime.strptime(doc['created_at'],'%a %b %d %H:%M:%S %z %Y')
#    db.mycollection.save(doc)


start = time.time()
#tweets = TweetsPerHour()
#tweets = TweetsDistinctLocation()
#tweets = TweetPercentWithWord("switch")
tweets = TweetPercentWithWord("sonic")
end = time.time()
print("result: " + str(tweets) + " time: " + str((end - start)* 1000) + "ms")
