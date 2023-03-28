from mongo_crud import insert_purchase
from schemas import UserPurchaseInsert
from kafka import KafkaConsumer
from consts import Config
from json import loads


def _send_message_to_mongo(message_dict):
    user_purchase = UserPurchaseInsert.parse_obj(message_dict)
    insert_purchase(user_purchase)


def _consume_from_kafka():
    consumer = KafkaConsumer(Config.Kafka.TOPIC,
                             bootstrap_servers=Config.Kafka.SERVERS,
                             api_version=(2, 5, 0),
                             auto_offset_reset='earliest',
                             enable_auto_commit=True,
                             group_id=Config.Kafka.CONSUMER_GROUP,
                             value_deserializer=lambda x: loads(x.decode('utf-8'))
                             )

    for message in consumer:
        _send_message_to_mongo(message.value)


def start_consumer():
    _consume_from_kafka()
