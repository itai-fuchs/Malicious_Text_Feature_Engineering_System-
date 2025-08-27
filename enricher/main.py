from config import producer, consumer,send_topic1, send_topic2, get_topic1, get_topic2
from enricher import Enricher



def consume_and_produce():
    for message in consumer:
        topic = message.topic
        doc = message.value
        original_text = doc.get("processed_text", "")
        enricher = Enricher(original_text)
        doc["sentiment"]=enricher.sentiment_analyzer()
        doc["weapons_list"]=enricher.find_weapon()
        doc["latest_timestamp"] =enricher.find_time_signature()

        if topic ==get_topic1:
            producer.send(send_topic1, doc)
        elif topic == get_topic2:
            producer.send(send_topic2, doc)


        producer.flush()