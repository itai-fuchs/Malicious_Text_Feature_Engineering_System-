import logging

#log config
logging.basicConfig(level=logging.ERROR)
#kafka config
KAFKA_BROKERS = ["localhost:9092"]

#topics config
get_topic_antisemitic = "preprocessed_tweets_antisemitic"
get_topic_not_antisemitic = "preprocessed_tweets_not_antisemitic"
send_topic_antisemitic = "enriched_preprocessed_tweets_antisemitic"
send_topic_not_antisemitic = "enriched_preprocessed_tweets_not_antisemitic"

# data config
data_path= "../data/weapon_list.txt"


#doc config

clean_text ="clean_text"
original_text ="text"


sentiment="sentiment"
weapons_detected ="weapons_detected"
relevant_timestamp = "relevant_timestamp"