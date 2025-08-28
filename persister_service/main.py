from consumer import TweetConsumer
from persister import Persister

def main():
    consumer = TweetConsumer()
    persister = Persister()


    for label, document in consumer.consume():
        persister.save(label, document)

if __name__ == "__main__":
    main()
