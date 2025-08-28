from kafka import KafkaConsumer, KafkaProducer
from config import KAFKA_BROKERS,get_topic_antisemitic,get_topic_not_antisemitic
import json, logging


logger = logging.getLogger(__name__)


def create_consumer():
    try:
        consumer = KafkaConsumer(
            get_topic_antisemitic, get_topic_not_antisemitic,
            bootstrap_servers=KAFKA_BROKERS,
            value_deserializer=lambda x: json.loads(x.decode("utf-8")),
            auto_offset_reset="earliest",
            enable_auto_commit=True
        )
        logger.info(f"KafkaConsumer subscribed to topics: {get_topic_antisemitic}, {get_topic_not_antisemitic}")

        return consumer
    except Exception as e:
        logger.error(f"Error creating KafkaConsumer: {e}")
        raise

def create_producer():
    try:
        producer = KafkaProducer(
            bootstrap_servers=KAFKA_BROKERS,
            value_serializer=lambda x: json.dumps(x).encode("utf-8")
        )
        logger.info("KafkaProducer created successfully")
        return producer
    except Exception as e:
        logger.error(f"Error creating KafkaProducer: {e}")
        raise