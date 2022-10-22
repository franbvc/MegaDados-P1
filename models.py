from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel, Field


class Product(BaseModel):
    """
    Product model
    """

    id: int = Field(example=1, description="Product ID")
    name: str = Field(example="Product 1", description="Product name")
    price: float = Field(example=10.0, description="Product price")
    quantity: int = Field(example=4, description="Product quantity")
    details: str = Field(example="Details 1", description="Product details")


class RequestProduct(BaseModel):
    """
    Request product model for POST and PUT requests
    """

    name: str = Field(example="Product 1", description="Product name")
    price: float = Field(example=10.0, description="Product price")
    quantity: int = Field(example=4, description="Product quantity")
    details: str = Field(example="Details 1", description="Product details")


class RequestProductQuantity(BaseModel):
    """
    Request product quantity model for PUT requests
    """

    quantity: int = Field(example=4, description="Product quantity")


class RequestProductDetails(BaseModel):
    """
    Request product details model for PUT requests
    """

    details: str = Field(example="Details 1", description="Product details")


class ErrorMessage(BaseModel):
    """
    Error message model
    """
    
    message: str = Field(example="Example message", description="Error message")
