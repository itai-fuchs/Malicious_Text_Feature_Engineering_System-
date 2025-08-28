import logging
from kafka import KafkaConsumer
import json
import config



logger = logging.getLogger(__name__)

try:
    consumer = KafkaConsumer(
        config.KAFKA_TOPICS["antisemitic"],
        config.KAFKA_TOPICS["not_antisemitic"],
        bootstrap_servers=config.KAFKA_BROKER,
        value_deserializer=lambda x: json.loads(x.decode("utf-8")),
        auto_offset_reset="earliest",
        enable_auto_commit=True
    )
    logger.info("Kafka consumer initialized successfully.")
except Exception as e:
    logger.error(f"Failed to initialize Kafka consumer: {e}")
    consumer = None
