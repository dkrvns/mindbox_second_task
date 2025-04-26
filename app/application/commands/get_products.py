from dataclasses import dataclass

from didiator import Query, QueryHandler

from app.application import dto
from app.application.interface.repository.product import ProductRepository


@dataclass(frozen=True)
class GetProducts(Query[dto.Products]):
    ...


class GetProductsHandler(QueryHandler[GetProducts, dto.Products]):
    def __init__(self, repo: ProductRepository) -> None:
        self._repo = repo

    async def __call__(self, query: GetProducts) -> dto.Products:
        products = await self._repo.get_products()
        return products
