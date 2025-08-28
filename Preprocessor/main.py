from config import producer, consumer
from utils import process_text




def consume_and_produce():
    for message in consumer:
        topic = message.topic
        data = message.value
        original_text = data.get("text", "")

        processed = process_text(original_text)
        data["processed_text"] = processed

        if topic == "raw_tweets_antisemitic":
            producer.send("preprocessed_tweets_antisemitic", data)
        elif topic == "raw_tweets_not_antisemitic":
            producer.send("preprocessed_tweets_not_antisemitic", data)


        producer.flush()
