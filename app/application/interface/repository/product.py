import abc

from app.application import dto


class ProductRepository(abc.ABC):
    @abc.abstractmethod
    async def get_products(self) -> dto.Products:
        ...
