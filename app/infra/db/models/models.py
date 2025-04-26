from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship

from app.infra.db.models.base import BaseModel

product_category_association = Table(
    'product_category',
    BaseModel.metadata,
    Column('product_id', Integer, ForeignKey('products.id')),
    Column('category_id', Integer, ForeignKey('categories.id'))
)

class Product(BaseModel):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    categories = relationship("Category", secondary=product_category_association, back_populates="products")

class Category(BaseModel):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    products = relationship("Product", secondary=product_category_association, back_populates="categories")
