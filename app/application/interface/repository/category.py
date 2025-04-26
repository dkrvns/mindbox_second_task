import abc

from app.application import dto


class CategoryRepository(abc.ABC):
    @abc.abstractmethod
    async def get_categories(self) -> dto.Categories:
        ...
