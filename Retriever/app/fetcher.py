from pymongo import MongoClient, errors
import config
import logging

# Create a logger for this module
logger = logging.getLogger(__name__)

class Fetcher:
    def __init__(self):
        # Holds the MongoDB connection. None if not connected yet.
        self.conn: MongoClient | None = None

    def open_conn(self):
        """
        Opens a MongoDB connection if not already open.
        """
        if self.conn is None:
            try:
                self.conn = MongoClient(config.MONGO_URI)
                logger.info("MongoDB connection opened successfully.")
            except errors.PyMongoError as e:
                logger.error(f"Failed to connect to MongoDB: {e}")
                self.conn = None
        return self.conn

    def get_collection(self):
        """
        Returns the collection object from the MongoDB database.

        """
        conn = self.open_conn()
        if conn:
            try:
                collection = conn[config.MONGO_DB][config.COLLECTION]
                logger.debug(f"Accessed collection {config.COLLECTION} in DB {config.MONGO_DB}.")
                return collection
            except Exception as e:
                logger.error(f"Failed to access collection {config.COLLECTION}: {e}")
                return None
        else:
            logger.error("No MongoDB connection available.")
            return None

    def close_conn(self):
        """
        Closes the MongoDB connection if it exists.
        """
        if self.conn is not None:
            try:
                self.conn.close()
                logger.info("MongoDB connection closed.")
            except Exception as e:
                logger.warning(f"Error while closing MongoDB connection: {e}")
            finally:
                self.conn = None
