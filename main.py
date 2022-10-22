from typing import List, Union

from fastapi import FastAPI, Response, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from models import *

tags_metadata = [
    {
        "name": "products",
        "description": "Operations with products.",
    },
]

app = FastAPI(
    title="ProductAPI",
    description="API for managing products",
    version="0.0.1",
    openapi_tags=tags_metadata,
)

products = [
    Product(id=1, name="Product 1", price=10.0, quantity=4, details="Details 1")
]


@app.post(
    "/products",
    response_model=Product,
    status_code=status.HTTP_201_CREATED,
    tags=["products"],
)
async def create_product(product: RequestProduct):
    """
    Create a new product

    - **product**: Product to create
    """

    product_id = len(products) + 1
    products.append(
        Product(
            id=product_id,
            name=product.name,
            price=product.price,
            quantity=product.quantity,
            details=product.details,
        )
    )
    return products[-1]


@app.get(
    "/products",
    response_model=List[Product],
    status_code=status.HTTP_200_OK,
    tags=["products"],
)
async def get_products():
    """
    Get all products
    """

    return products


@app.patch(
    "/products/{product_id}/quantity",
    response_model=Product,
    status_code=status.HTTP_200_OK,
    responses={404: {"model": ErrorMessage}},
    tags=["products"],
)
async def update_product_quantity(
    product_id: int, product_quantity: RequestProductQuantity
):
    """
    Update product quantity

    - **product_id**: ID of the product to update
    - **product_quantity**: New quantity of the product
    """

    for product in products:
        if product.id == product_id:
            product.quantity = product_quantity.quantity
            return Response(content=product, status_code=status.HTTP_200_OK)

    return JSONResponse(
        content={"message": "Product not found"},
        status_code=status.HTTP_404_NOT_FOUND,
    )


@app.patch(
    "/products/{product_id}/details",
    response_model=Product,
    status_code=status.HTTP_200_OK,
    responses={404: {"model": ErrorMessage}},
    tags=["products"],
)
async def update_product_details(
    product_id: int,
    product_details: RequestProductDetails,
):
    """
    Update product details

    - **product_id**: ID of the product to update
    - **product_details**: New details of the product
    """

    for product in products:
        if product.id == product_id:
            product.details = product_details.details
            return product

    return JSONResponse(
        content={"message": "Product not found"},
        status_code=status.HTTP_404_NOT_FOUND,
    )


@app.put(
    "/products/{product_id}",
    response_model=Product,
    status_code=status.HTTP_200_OK,
    responses={404: {"model": ErrorMessage}},
    tags=["products"],
)
async def update_product(product_id: int, product_request: RequestProduct):
    """
    Update product

    - **product_id**: ID of the product to update
    - **product_request**: New product
    """

    for product in products:
        if product.id == product_id:
            product.name = product_request.name
            product.price = product_request.price
            product.quantity = product_request.quantity
            product.details = product_request.details
            return product

    return JSONResponse(
        content={"message": "Product not found"},
        status_code=status.HTTP_404_NOT_FOUND,
    )


@app.delete(
    "/products/{product_id}",
    response_model=Product,
    status_code=status.HTTP_200_OK,
    responses={404: {"model": ErrorMessage}},
    tags=["products"],
)
async def delete_product(product_id: int):
    """
    Delete product

    - **product_id**: ID of the product to delete
    """
    
    for product in products:
        if product.id == product_id:
            products.remove(product)
            return {"message": "Product deleted"}

    return JSONResponse(
        content={"message": "Product not found"},
        status_code=status.HTTP_404_NOT_FOUND,
    )
