import logging
from kafka_client import consumer
import config
from persist import Persister


logger = logging.getLogger(__name__)

persister = Persister()

def consume_and_save():
    logger.info("Starting Kafka consumption loop...")
    try:
        for message in consumer:
            try:
                topic = message.topic
                data = message.value

                label = "antisemitic" if topic == config.KAFKA_TOPICS["antisemitic"] else "not_antisemitic"
                persister.save(label, data)
                logger.info(f"Message saved to {label} collection: {data}")
            except Exception as msg_err:
                logger.error(f"Failed to process/save message: {msg_err}, data: {message.value}")
    except Exception as e:
        logger.error(f"Error during Kafka consumption loop: {e}")

if __name__ == "__main__":
    consume_and_save()
