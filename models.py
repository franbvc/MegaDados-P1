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
    details: str = Field(example="Details 1", description="Product details")


class Transaction(BaseModel):
    """
    Transaction model
    """

    id: int = Field(example=1, description="Transaction ID")
    product_id: int = Field(example=1, description="Product ID")
    transaction_date: str = Field(
        example="2020-01-01 13:12:11", description="Transaction date"
    )
    quantity: int = Field(example=4, description="Transaction quantity")
    transation_type: str = Field(example="BUY", description="Transaction type")


class RequestTransaction(BaseModel):
    """
    Request transaction model for POST requests
    """

    product_id: int = Field(example=1, description="Product ID")
    quantity: int = Field(example=4, description="Transaction quantity")


class RequestProductDetails(BaseModel):
    """
    Request product details model for PUT requests
    """

    details: str = Field(example="Details 1", description="Product details")


class RequestProductPrice(BaseModel):
    """
    Request product price model for PUT requests
    """

    price: float = Field(example=10.0, description="Product price")


class RequestProductName(BaseModel):
    """
    Request product name model for PUT requests
    """

    name: str = Field(example="Product 1", description="Product name")


class ErrorMessage(BaseModel):
    """
    Error message model
    """

    message: str = Field(example="Example message", description="Error message")
