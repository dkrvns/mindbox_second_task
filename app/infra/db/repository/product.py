from typing import Iterable

from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.application import dto
from app.application.interface.repository.product import ProductRepository
from app.infra.db.mappers.db_product_to_dto import convert_db_event_model_to_dto
from app.infra.db.models.models import Product
from app.infra.db.repository.base import SqlAlchemyRepository


class ProductRepositoryImpl(SqlAlchemyRepository, ProductRepository):
    async def get_products(self) -> dto.Products:
        query = select(Product).options(selectinload(Product.categories))

        res: Iterable[Product] = await self.session.scalars(query)

        products = [convert_db_event_model_to_dto(product) for product in res]

        return dto.Products(
            data=products,
        )
