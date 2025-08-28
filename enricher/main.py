import config
from enricher import Enricher
from kafka_client import consumer, producer
import logging
logger = logging.getLogger(__name__)




def consume_and_produce():

    for message in consumer:
        try:
            topic = message.topic
            doc = message.value
            clean_text = doc.get(config.clean_text, "")
            original_text = doc.get(config.original_text, "")

            # Enrich the message

            doc[config.sentiment] = Enricher.sentiment_analyzer(original_text)
            doc[config.weapons_detected] = Enricher.find_weapon(clean_text)
            doc[config.relevant_timestamp] = Enricher.latest_timestamp(original_text)

            # Determine send topic
            if topic == config.get_topic_antisemitic:
                producer.send(config.send_topic_antisemitic, doc)
            elif topic == config.get_topic_not_antisemitic:
                producer.send(config.send_topic_not_antisemitic, doc)
            else:
                logger.warning(f"Unknown topic: {topic}")



        except Exception as e:
            logger.error(f"Error processing message: {e}")

    # Flush once after processing all messages
    try:
        producer.flush()
        logger.info(f"Processed and sent messages")
    except Exception as e:
        logger.error(f"Error flushing producer: {e}")




consume_and_produce()