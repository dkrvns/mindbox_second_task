from dataclasses import dataclass

from didiator import Query, QueryHandler

from app.application import dto
from app.application.mapper.raw_data_to_dto_pairs import raw_data_to_dto_pairs


@dataclass(frozen=True)
class GetPairs(Query[dto.Categories]):
    categories: dto.Categories
    products: dto.Products


class GetPairsHandler(QueryHandler[GetPairs, dto.Pairs]):
    def __init__(self) -> None:
        ...


    async def __call__(self, query: GetPairs) -> dto.Pairs:
        products = query.products.data
        categories = query.categories.data

        category_name_map = {category.id: category.name for category in categories}

        pairs = [
            raw_data_to_dto_pairs(
                product.name,
                category_name_map.get(product.categories[0].id)
            if product.categories else None
            )
            for product in products
        ]
        return dto.Pairs(
            data=pairs
        )
