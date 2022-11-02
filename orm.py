from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DECIMAL, TEXT, DATETIME, ForeignKey

Base = declarative_base()


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    quantity = Column(Integer, nullable=False)
    details = Column(TEXT, nullable=False)

    def __repr__(self):
        return f"Product: {self.name}"


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(
        Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False
    )
    transaction_date = Column(DATETIME(), nullable=False)
    quantity = Column(Integer, nullable=False)
    type = Column(String(255), nullable=False)

    def __repr__(self):
        return f"Transaction: {self.id}"
