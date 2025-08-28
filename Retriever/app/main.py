from kafka_client import create_producer
from document_processor import DocumentProcessor
import config
import schedule
import time
import logging


processor=DocumentProcessor()
producer=create_producer()

logger = logging.getLogger(__name__)



def publish(topic1=config.anti_topic,topic2=config.not_anti_topic):
    global producer
    docs=processor.read_documents()
    if not docs:
        logger.info("No new documents to publish.")
        return
    topic1_count = 0
    topic2_count = 0
    for doc in docs:
        try:
            if doc.get(config.Classification_filed) == 1:
                producer.send(topic1, doc)
                topic1_count += 1
            else:
                producer.send(topic2, doc)
                topic2_count += 1

        except Exception as e:
            logger.error(f"Failed to publish document: {e}")

    producer.flush()
    logger.info(f"Published {topic1_count} docs to {topic1}, {topic2_count} docs to {topic2}")

    try:
        processor.fetcher.close_conn()
        logger.info("MongoDB connection closed after publishing.")
    except Exception as e:
        logger.warning(f"Failed to close MongoDB connection: {e}")





publish()
schedule.every(1).minutes.do(publish)

while True:


    schedule.run_pending()
    time.sleep(1)






