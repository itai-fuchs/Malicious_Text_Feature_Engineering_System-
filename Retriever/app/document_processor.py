import logging
from config import time_filed, Classification_filed, limit
from fetcher import Fetcher

logger = logging.getLogger(__name__)

class DocumentProcessor:
    def __init__(self):
        self.fetcher = Fetcher()
        self.last_time = None

    def read_documents(self):
        """
        Reads documents from MongoDB
        """
        try:
            collection = self.fetcher.get_collection()
            if collection is None:
                logger.error("No collection available to read documents.")
                return []

            docs = list(collection.find(
                {time_filed: {"$gt": self.last_time}} if self.last_time else {},
                {"_id": 0}
            ).sort(time_filed, 1).limit(limit))

            if docs:
                self.last_time = docs[-1][time_filed]

            logger.info(f"Fetched {len(docs)} documents. Last time updated to {self.last_time}")
            return docs

        except Exception as e:
            logger.error(f"Error reading documents: {e}")
            return []
