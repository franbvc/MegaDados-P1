from typing import List
from dotenv import load_dotenv

import os
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from datetime import datetime

from models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from orm import Product as ProductORM, Transaction as TransactionORM

load_dotenv()

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

engine = create_engine(os.environ["DB_URL"], echo=True)

Session = sessionmaker(bind=engine)
session = Session()


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

    new_orm_product = ProductORM(
        name=product.name,
        price=product.price,
        quantity=0,
        details=product.details,
    )

    session.add(new_orm_product)
    session.commit()

    new_product = Product(
        id=new_orm_product.id,
        name=new_orm_product.name,
        price=new_orm_product.price,
        quantity=new_orm_product.quantity,
        details=new_orm_product.details,
    )

    return new_product


@app.post(
    "/transactions",
    response_model=Transaction,
    status_code=status.HTTP_201_CREATED,
    responses={404: {"model": ErrorMessage}, 400: {"model": ErrorMessage}},
    tags=["products"],
)
async def create_transaction(transaction: RequestTransaction):
    """
    Create a new transaction

    - **transaction**: Transaction to create
    """
    product_orm = session.query(ProductORM).filter_by(id=transaction.product_id).first()

    if product_orm is None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Product not found"},
        )

    if transaction.quantity == 0:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": "Quantity cannot be zero"},
        )

    if transaction.quantity + product_orm.quantity < 0:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": "Not enough product quantity"},
        )

    new_orm_transaction = TransactionORM(
        product_id=transaction.product_id,
        transaction_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        quantity=transaction.quantity,
        type="BUY" if transaction.quantity > 0 else "SELL",
    )

    product_orm.quantity += transaction.quantity

    session.add(new_orm_transaction)
    session.commit()

    new_transaction = Transaction(
        id=new_orm_transaction.id,
        product_id=new_orm_transaction.product_id,
        transaction_date=str(new_orm_transaction.transaction_date),
        quantity=new_orm_transaction.quantity,
        transation_type=new_orm_transaction.type,
    )

    return new_transaction


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

    products_orm = session.query(ProductORM).all()

    products = []

    for product_orm in products_orm:
        product = Product(
            id=product_orm.id,
            name=product_orm.name,
            price=product_orm.price,
            quantity=product_orm.quantity,
            details=product_orm.details,
        )

        products.append(product)

    return products


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

    product_orm = session.query(ProductORM).filter_by(id=product_id).first()

    if product_orm is None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Product not found"},
        )

    product_orm.details = product_details.details

    session.commit()

    product = Product(
        id=product_orm.id,
        name=product_orm.name,
        price=product_orm.price,
        quantity=product_orm.quantity,
        details=product_orm.details,
    )

    return product


@app.patch(
    "/products/{product_id}/price",
    response_model=Product,
    status_code=status.HTTP_200_OK,
    responses={404: {"model": ErrorMessage}},
    tags=["products"],
)
async def update_product_price(
    product_id: int,
    product_price: RequestProductPrice,
):
    """
    Update product details

    - **product_id**: ID of the product to update
    - **product_price**: New details of the product
    """

    product_orm = session.query(ProductORM).filter_by(id=product_id).first()

    if product_orm is None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Product not found"},
        )

    product_orm.price = product_price.price

    session.commit()

    product = Product(
        id=product_orm.id,
        name=product_orm.name,
        price=product_orm.price,
        quantity=product_orm.quantity,
        details=product_orm.details,
    )

    return product


@app.patch(
    "/products/{product_id}/name",
    response_model=Product,
    status_code=status.HTTP_200_OK,
    responses={404: {"model": ErrorMessage}},
    tags=["products"],
)
async def update_product_name(
    product_id: int,
    product_name: RequestProductName,
):
    """
    Update product details

    - **product_id**: ID of the product to update
    - **product_price**: New details of the product
    """

    product_orm = session.query(ProductORM).filter_by(id=product_id).first()

    if product_orm is None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Product not found"},
        )

    product_orm.name = product_name.name

    session.commit()

    product = Product(
        id=product_orm.id,
        name=product_orm.name,
        price=product_orm.price,
        quantity=product_orm.quantity,
        details=product_orm.details,
    )

    return product


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
    product_orm = session.query(ProductORM).filter(ProductORM.id == product_id).first()

    if product_orm is None:
        return JSONResponse(
            content={"message": "Product not found"},
            status_code=status.HTTP_404_NOT_FOUND,
        )

    product_orm.name = product_request.name
    product_orm.price = product_request.price
    product_orm.details = product_request.details

    session.commit()

    product = Product(
        id=product_orm.id,
        name=product_orm.name,
        price=product_orm.price,
        quantity=product_orm.quantity,
        details=product_orm.details,
    )

    return product


@app.delete(
    "/products/{product_id}",
    status_code=status.HTTP_200_OK,
    responses={404: {"model": ErrorMessage}},
    tags=["products"],
)
async def delete_product(product_id: int):
    """
    Delete product

    - **product_id**: ID of the product to delete
    """
    product_orm = session.query(ProductORM).filter(ProductORM.id == product_id).first()

    if product_orm is None:
        return JSONResponse(
            content={"message": "Product not found"},
            status_code=status.HTTP_404_NOT_FOUND,
        )

    session.delete(product_orm)
    session.commit()
