from pydantic import BaseModel, Field
from datetime import datetime


class UserPurchaseInsert(BaseModel):
    username: str = Field(...)
    user_id: int = Field(...)
    price: float = Field(...)
    product: str = Field(...)
    timestamp: datetime = datetime.now()
