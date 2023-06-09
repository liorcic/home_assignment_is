from schemas import UserPurchaseInsert
from random_word import RandomWords
from datetime import datetime
import random

r = RandomWords()


def get_random_word():
    return r.get_random_word()


def generate_random_buy() -> UserPurchaseInsert:
    username = get_random_word()
    user_id = random.randint(1, 10)
    price = random.random() * random.randint(1, 100)
    product = get_random_word()
    purchase = UserPurchaseInsert(username=username,
                                  user_id=user_id,
                                  price=price,
                                  product=product,
                                  timestamp=datetime.now())
    return purchase
