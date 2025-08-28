KAFKA_BROKER = "localhost:9092"

KAFKA_TOPICS = {
    "antisemitic": "enriched_preprocessed_tweets_antisemitic",
    "not_antisemitic": "enriched_preprocessed_tweets_not_antisemitic"
}

MONGO_URI = "mongodb://localhost:27017/"
MONGO_DB = "tweets_db"

MONGO_COLLECTIONS = {
    "antisemitic": "tweets_antisemitic",
    "not_antisemitic": "tweets_not_antisemitic"
}
