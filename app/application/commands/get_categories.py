from dataclasses import dataclass

from didiator import QueryHandler, Query

from app.application import dto
from app.application.interface.repository.category import CategoryRepository


@dataclass(frozen=True)
class GetCategories(Query[dto.Categories]):
    ...


class GetCategoriesHandler(QueryHandler[GetCategories, dto.Categories]):
    def __init__(self, repo: CategoryRepository) -> None:
        self._repo = repo

    async def __call__(self, query: GetCategories) -> dto.Categories:
        categories = await self._repo.get_categories()
        return categories
