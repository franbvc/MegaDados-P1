from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel, Field


class Product(BaseModel):
    id: int = Field(example=1, description="Product ID")
    name: str = Field(example="Product 1", description="Product name")
    price: float = Field(example=10.0, description="Product price")
    quantity: int = Field(example=4, description="Product quantity")
    details: str = Field(example="Details 1", description="Product details")


class RequestProduct(BaseModel):
    name: str = Field(example="Product 1", description="Product name")
    price: float = Field(example=10.0, description="Product price")
    quantity: int = Field(example=4, description="Product quantity")
    details: str = Field(example="Details 1", description="Product details")


class RequestProductQuantity(BaseModel):
    quantity: int = Field(example=4, description="Product quantity")


class RequestProductDetails(BaseModel):
    details: str = Field(example="Details 1", description="Product details")


class ErrorMessage(BaseModel):
    message: str = Field(example="Example message", description="Error message")
