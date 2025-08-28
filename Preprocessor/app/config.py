import logging

logger = logging.getLogger(__name__)

#loger config
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

# kafka config
get_topic_antisemitic= "raw_tweets_antisemitic"
get_topic_not_antisemitic= "raw_tweets_not_antisemitic"
send_topic_antisemitic= "preprocessed_tweets_antisemitic"
send_topic_not_antisemitic= "preprocessed_tweets_not_antisemitic"
KAFKA_BROKERS=["broker:9092"]



clean_text ="clean_text"
original_text ="text"