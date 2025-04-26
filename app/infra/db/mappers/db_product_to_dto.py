from app.application import dto
from app.infra.db.models.models import Product


def convert_db_event_model_to_dto(product: Product) -> dto.Product:
    return dto.Product(
        id=product.id,
        name=product.name,
        categories=product.categories,
    )
