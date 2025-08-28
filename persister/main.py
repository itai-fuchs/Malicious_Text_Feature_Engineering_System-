from kafka_client import consumer
import config
from persister.persist import Persister

persister = Persister()

def consume_and_save():
    for message in consumer:
        topic = message.topic
        data = message.value

        label = "antisemitic" if topic == config.KAFKA_TOPICS["antisemitic"] else "not_antisemitic"
        persister.save(label, data)


consume_and_save()
