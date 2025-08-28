from pymongo import MongoClient
import config

class Persister:
    def __init__(self):
        client = MongoClient(config.MONGO_URI)
        self.db = client[config.MONGO_DB]
        self.collections = {
            "antisemitic": self.db[config.MONGO_COLLECTIONS["antisemitic"]],
            "not_antisemitic": self.db[config.MONGO_COLLECTIONS["not_antisemitic"]],
        }

    def save(self, label, document):
        if label not in self.collections:
            raise ValueError(f"Unknown label: {label}")
        self.collections[label].insert_one(document)

