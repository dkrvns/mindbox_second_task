from app.application import dto
from app.infra.db.models.models import Category


def convert_db_event_model_to_dto(category: Category) -> dto.Category:
    return dto.Category(
        id=category.id,
        name=category.name,
        products=category.products,
    )
