import logging
import config
from kafka_client import consumer, producer
from utils import process_text

logger = logging.getLogger(__name__)

def consume_and_produce():
    if not consumer or not producer:
        logger.error("Kafka consumer or producer is not initialized.")
        return

    try:
        for message in consumer:
            try:
                topic = message.topic
                data = message.value
                original_text = data.get(config.original_text, "")
                data[config.clean_text] = process_text(original_text)

                if topic == config.get_topic_antisemitic:
                    producer.send(config.send_topic_antisemitic, data)
                elif topic == config.get_topic_not_antisemitic:
                    producer.send(config.send_topic_not_antisemitic, data)

                producer.flush()

            except Exception:
                logger.exception("Failed to process or send message.")
    except Exception:
        logger.exception("Critical error during Kafka consumption loop.")

if __name__ == "__main__":
    consume_and_produce()
