from bson import ObjectId
from pydantic import BaseModel, Field
from datetime import datetime


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class UserPurchaseInsert(BaseModel):
    username: str = Field(...)
    user_id: int = Field(...)
    price: float = Field(...)
    product: str = Field(...)
    timestamp: datetime


class UserPurchaseOutput(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    username: str = Field(...)
    user_id: int = Field(...)
    price: float = Field(...)
    product: str = Field(...)
    timestamp: datetime

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
