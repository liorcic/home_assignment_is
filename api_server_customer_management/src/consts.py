from os import getenv
from json import loads


class Config:
    class Kafka:
        TOPIC = getenv("KAFKA_TOPIC")
        CONSUMER_GROUP = getenv("KAFKA_CONSUMER")
        SERVERS = loads(getenv("KAFKA_BROKERS"))

    class Mongo:
        CONNECTION_STRING = getenv("MONGO_DB_URL")
        DB_NAME = getenv("MONGO_DB_NAME")
        PURCHASE_COLLECTION = "users_purchases"

    class Server:
        HOST = "0.0.0.0"
        PORT = 8000
