import logging
import json
from kafka import KafkaConsumer, KafkaProducer
import config

logger = logging.getLogger(__name__)

# Consumer
try:
    consumer = KafkaConsumer(
        config.get_topic_antisemitic, config.get_topic_not_antisemitic,
        bootstrap_servers=config.KAFKA_BROKERS,
        value_deserializer=lambda x: json.loads(x.decode("utf-8")),
        auto_offset_reset="earliest",
        enable_auto_commit=True
    )
except Exception as e:
    logger.error(f"Failed to initialize Kafka consumer: {e}")
    consumer = None

# Producer
try:
    producer = KafkaProducer(
        bootstrap_servers=config.KAFKA_BROKERS,
        value_serializer=lambda x: json.dumps(x).encode("utf-8")
    )
except Exception as e:
    logger.error(f"Failed to initialize Kafka producer: {e}")
    producer = None
