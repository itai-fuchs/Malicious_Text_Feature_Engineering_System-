from kafka import KafkaConsumer, KafkaProducer
from config import KAFKA_BROKERS
import json
import logging

logger = logging.getLogger(__name__)

def create_producer():
    try:
        producer = KafkaProducer(
            bootstrap_servers=KAFKA_BROKERS,
            value_serializer=lambda x: json.dumps(x, default=str).encode('utf-8')
        )
        logger.info("Kafka Producer initialized successfully.")
        return producer
    except Exception as e:
        logger.error(f"Failed to initialize Kafka Producer: {e}")
        producer = None


