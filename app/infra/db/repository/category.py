from typing import Iterable

from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.application import dto
from app.application.interface.repository.category import CategoryRepository
from app.infra.db.mappers.db_category_to_dto import convert_db_event_model_to_dto
from app.infra.db.models.models import Category
from app.infra.db.repository.base import SqlAlchemyRepository


class CategoryRepositoryImpl(SqlAlchemyRepository, CategoryRepository):
    async def get_categories(self) -> dto.Categories:
        query = select(Category).options(selectinload(Category.products))

        res: Iterable[Category] = await self.session.scalars(query)

        categories = [convert_db_event_model_to_dto(category) for category in res]

        return dto.Categories(
            data=categories,
        )
