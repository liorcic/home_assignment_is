from kafka_process import start_consumer
from schemas import UserPurchaseOutput
from fastapi import FastAPI
from typing import List
from consts import Config
import multiprocessing
import mongo_crud
import uvicorn


app = FastAPI()


@app.get("/isAlive")
def is_alive():
    return "API server for customer management is alive"


@app.get("/buyList/{user_id}", response_model=List[UserPurchaseOutput])
async def get_buy_list(user_id: int):
    return await mongo_crud.get_purchases_for_user(user_id)


@app.get("/buyList", response_model=List[UserPurchaseOutput])
async def get_buy_list():
    return await mongo_crud.get_all_purchases()


def main():
    process = multiprocessing.Process(target=start_consumer)
    process.start()

    uvicorn.run("main:app", host=Config.Server.HOST, port=Config.Server.PORT)


if __name__ == '__main__':
    print("Hello")
    main()
