from pydantic import BaseModel, Field


class User(BaseModel):
    id: int = Field(alias="_id")
    name: str
    email: str


class Product(BaseModel):
    id: int = Field(alias="_id")
    name: str
    price: float
