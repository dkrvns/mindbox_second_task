from dataclasses import dataclass

from app.application.dto.base import ListItemsDTO


@dataclass(frozen=True)
class Category:
    id: int
    name: str
    products: list[str]

Categories = ListItemsDTO[Category]
