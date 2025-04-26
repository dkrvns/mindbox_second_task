from dataclasses import dataclass

from app.application.dto.base import ListItemsDTO


@dataclass(frozen=True)
class Pair:
    product_name: str
    category_name: str

Pairs = ListItemsDTO[Pair]
