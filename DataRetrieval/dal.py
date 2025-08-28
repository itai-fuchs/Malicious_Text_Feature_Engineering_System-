from pymongo import MongoClient
import config
import logging

logging.basicConfig(level=logging.ERROR)

class TweetRepository:
    def __init__(self):
        try:
            client = MongoClient(config.MONGO_URI)
            self.db = client[config.MONGO_DB]
        except Exception as e:
            logging.error(f"Failed to connect to MongoDB: {e}")
            raise

    def get_tweets(self, label):
        try:
            if label not in config.COLLECTIONS:
                raise ValueError(f"Unknown label: {label}")
            collection = self.db[config.COLLECTIONS[label]]
            return list(collection.find({}, {"_id": 0}))
        except Exception as e:
            logging.error(f"Error while retrieving tweets for label '{label}': {e}")
            raise
