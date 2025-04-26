from dataclasses import dataclass

from app.application.dto.base import ListItemsDTO


@dataclass(frozen=True)
class Product:
    id: int
    name: str
    categories: list[str]

Products = ListItemsDTO[Product]
