from json import loads
from os import getenv


class Config:
    class Kafka:
        TOPIC = getenv("KAFKA_TOPIC")
        SERVERS = loads(getenv("KAFKA_BROKERS"))

    class ManagingAPI:
        URL = getenv("MANAGING_API_URL")

    class Server:
        HOST = "0.0.0.0"
        PORT = 8000
