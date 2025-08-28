import json
from kafka import KafkaConsumer, KafkaProducer


consumer = KafkaConsumer(
    "raw_tweets_antisemitic", "raw_tweets_not_antisemitic",
    bootstrap_servers=["localhost:9092"],
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    auto_offset_reset="earliest",
    enable_auto_commit=True
)

# Producer
producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    value_serializer=lambda x: json.dumps(x).encode("utf-8")
)
