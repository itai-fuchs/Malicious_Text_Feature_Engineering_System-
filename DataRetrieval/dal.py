from pymongo import MongoClient
import config

class TweetRepository:
    def __init__(self):
        client = MongoClient(config.MONGO_URI)
        self.db = client[config.MONGO_DB]

    def get_tweets(self, label):
        if label not in config.COLLECTIONS:
            raise ValueError(f"Unknown label: {label}")
        collection = self.db[config.COLLECTIONS[label]]
        return list(collection.find({}, {"_id": 0}))
