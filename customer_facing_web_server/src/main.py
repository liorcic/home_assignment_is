from fastapi.middleware.cors import CORSMiddleware
from schemas import UserPurchaseInsert
from utils import generate_random_buy
from kafka import KafkaProducer
from fastapi import FastAPI
from consts import Config
import requests
import uvicorn
import json

app = FastAPI()

# Accepts requests from the front end react component
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

producer = KafkaProducer(bootstrap_servers=Config.Kafka.SERVERS,
                         value_serializer=lambda x: json.dumps(x, default=str).encode('utf-8'),
                         api_version=(2, 5, 0)
                         )


@app.get("/isAlive")
def is_alive():
    return "Im alive"


@app.get("/buyList/{user_id}")
def get_buy_list(user_id: int):
    result = requests.get(f"{Config.ManagingAPI.URL}/buyList/{user_id}")
    return result.json()

@app.get("/buyList")
def get_buy_list():
    result = requests.get(f"{Config.ManagingAPI.URL}/buyList")
    return result.json()

@app.post("/buy", response_model=UserPurchaseInsert, status_code=201)
def produce_to_kafka():
    purchase_obj = generate_random_buy()
    print(f"Sending {purchase_obj}")
    producer.send(Config.Kafka.TOPIC, purchase_obj.dict())
    producer.flush()
    return purchase_obj


def main():
    uvicorn.run("main:app", host=Config.Server.HOST, port=Config.Server.PORT)


if __name__ == '__main__':
    main()
