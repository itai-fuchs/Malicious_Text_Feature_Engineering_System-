from config import send_topic_antisemitic, send_topic_not_antisemitic,get_topic_antisemitic, get_topic_not_antisemitic
from enricher import Enricher
from kafka_client import create_consumer, create_producer

logger = logging.getLogger(__name__)




consumer = create_consumer()
producer = create_producer()


def consume_and_produce():

    for message in consumer:
        try:
            topic = message.topic
            doc = message.value
            original_text = doc.get("clean_text", "")

            # Enrich the message
            enricher = Enricher(original_text)
            doc["sentiment"] = enricher.sentiment_analyzer()
            doc["weapons_detected"] = enricher.find_weapon()
            doc["relevant_timestamp"] = enricher.latest_timestamp()

            # Determine send topic
            if topic == get_topic_antisemitic:
                producer.send(send_topic_antisemitic, doc)
            elif topic == get_topic_not_antisemitic:
                producer.send(send_topic_not_antisemitic, doc)
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