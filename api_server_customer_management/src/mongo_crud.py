from schemas import UserPurchaseInsert, UserPurchaseOutput
import motor.motor_asyncio
from consts import Config
from typing import List


client = motor.motor_asyncio.AsyncIOMotorClient(Config.Mongo.CONNECTION_STRING)
db = client[Config.Mongo.DB_NAME]
purchase_collection = db[Config.Mongo.PURCHASE_COLLECTION]


async def get_all_purchases() -> List[UserPurchaseOutput]:
    all_purchases = await purchase_collection.find().to_list(1000)
    return all_purchases


async def get_purchases_for_user(user_id: int) -> List[UserPurchaseOutput]:
    all_purchases = await purchase_collection.find({"user_id": user_id}).to_list(1000)
    return all_purchases


def insert_purchase(user_purchase: UserPurchaseInsert):
    purchase_collection.insert_one(user_purchase.dict())
