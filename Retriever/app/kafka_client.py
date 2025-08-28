from kafka import KafkaConsumer, KafkaProducer
import config
import json
import logging

logger = logging.getLogger(__name__)

def create_producer():
    try:
        producer = KafkaProducer(
            bootstrap_servers=config.KAFKA_BROKERS,
            value_serializer=lambda x: json.dumps(x, default=str).encode('utf-8')
        )
        logger.info("Kafka Producer initialized successfully.")

    except Exception as e:
        logger.error(f"Failed to initialize Kafka Producer: {e}")
        producer = None

    return producer

