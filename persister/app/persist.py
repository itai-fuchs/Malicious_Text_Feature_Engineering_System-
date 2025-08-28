import logging
from pymongo import MongoClient, errors
import config

logger = logging.getLogger(__name__)

class Persister:
    def __init__(self):
        try:
            client = MongoClient(config.MONGO_URI)
            self.db = client[config.MONGO_DB]
            self.collections = {
                "antisemitic": self.db[config.MONGO_COLLECTIONS["antisemitic"]],
                "not_antisemitic": self.db[config.MONGO_COLLECTIONS["not_antisemitic"]],
            }
        except errors.PyMongoError as e:
            logger.error(f"Failed to connect to MongoDB: {e}")
            self.db = None
            self.collections = {}

    def save(self, label, document):
        if not self.collections:
            logger.error("No MongoDB collections available. Document not saved.")
            return

        if label not in self.collections:
            logger.error(f"Unknown label: {label}. Document not saved.")
            return

        try:
            self.collections[label].insert_one(document)
        except errors.PyMongoError as e:
            logger.error(f"Failed to insert document into '{label}' collection: {e}")
