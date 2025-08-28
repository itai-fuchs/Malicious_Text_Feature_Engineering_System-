from kafka import KafkaConsumer, KafkaProducer
import config
import json, logging


logger = logging.getLogger(__name__)



try:
    consumer = KafkaConsumer(
        config.get_topic_antisemitic, config.get_topic_not_antisemitic,
        bootstrap_servers=config.KAFKA_BROKERS,
        value_deserializer=lambda x: json.loads(x.decode("utf-8")),
        auto_offset_reset="earliest",
        enable_auto_commit=True
    )
    logger.info(f"KafkaConsumer subscribed to topics: {config.get_topic_antisemitic}, {config.get_topic_not_antisemitic}")

except Exception as e:
    logger.error(f"Error creating KafkaConsumer: {e}")



try:
    producer = KafkaProducer(
        bootstrap_servers=config.KAFKA_BROKERS,
        value_serializer=lambda x: json.dumps(x).encode("utf-8")
    )
    logger.info("KafkaProducer created successfully")

except Exception as e:
    logger.error(f"Error creating KafkaProducer: {e}")
