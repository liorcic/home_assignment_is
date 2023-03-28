from schemas import UserPurchaseInsert
from random_word import RandomWords
import random

r = RandomWords()


def get_random_word():
    return r.get_random_word()


def generate_random_buy() -> UserPurchaseInsert:
    username = get_random_word()
    user_id = random.randint(1, 1000)
    price = random.random() * random.randint(1, 100)
    product = get_random_word()
    purchase = UserPurchaseInsert(username=username,
                                  user_id=user_id,
                                  price=price,
                                  product=product)
    return purchase
