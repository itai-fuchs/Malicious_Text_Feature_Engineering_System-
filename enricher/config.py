import json
from main import KafkaConsumer, KafkaProducer

get_topic1= "preprocessed_tweets_antisemitic"
get_topic2="preprocessed_tweets_not_antisemitic"
send_topic1="enriched_preprocessed_tweets_antisemitic"
send_topic2="enriched_preprocessed_tweets_not_antisemitic"
consumer = KafkaConsumer(
    topic1, topic2,
    bootstrap_servers=["localhost:9092"],
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    auto_offset_reset="earliest",
    enable_auto_commit=True
)


producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    value_serializer=lambda x: json.dumps(x).encode("utf-8")
)