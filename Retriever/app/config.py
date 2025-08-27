import os
from kafka import KafkaProducer
import json
import logging

# Logger setup
logging.basicConfig(level=logging.WARNING, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

# MongoDB config
MONGO_DB   = os.getenv("MONGO_DB", "IranMalDB")
MONGO_USER = os.getenv("MONGO_USER", "IRGC_NEW")
MONGO_PASS = os.getenv("MONGO_PASS", "iran135")
MONGO_HOST = os.getenv("MONGO_HOST", "cluster0.6ycjkak.mongodb.net")
COLLECTION = os.getenv("MONGO_COLLECTION", "tweets")

MONGO_URI = os.getenv(
    "MONGO_URI",
    f"mongodb+srv://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}/{MONGO_DB}?retryWrites=true&w=majority"
)
logger.info(f"MongoDB URI configured for DB: {MONGO_DB}, Collection: {COLLECTION}")

# Processor config
Classification_filed = "Antisemitic"
limit = 100
time_filed = "CreateDate"

# Kafka config
try:
    producer = KafkaProducer(
        bootstrap_servers=['broker:9092'],
        value_serializer=lambda x: json.dumps(x, default=str).encode('utf-8')
    )
    logger.info("Kafka Producer initialized successfully.")
except Exception as e:
    logger.error(f"Failed to initialize Kafka Producer: {e}")
    producer = None

anti_topic="raw_tweets_antisemitic"
not_anti_topic="raw_tweets_not_antisemitic"