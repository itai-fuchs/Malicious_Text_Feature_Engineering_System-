import config
from kafka_client import consumer,producer
from utils import process_text




def consume_and_produce():
    for message in consumer:
        topic = message.topic
        data = message.value
        original_text = data.get(config.original_text, "")

        processed = process_text(original_text)
        data[config.clean_text] = processed

        if topic == config.get_topic_antisemitic:
            producer.send(config.send_topic_antisemitic, data)
        elif topic == config.get_topic_not_antisemitic:
            producer.send(config.send_topic_not_antisemitic, data)


        producer.flush()

consume_and_produce()