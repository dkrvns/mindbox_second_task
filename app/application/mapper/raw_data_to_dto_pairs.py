from app.application import dto


def raw_data_to_dto_pairs(product_name: str, category_name: str) -> dto.Pair:
    return dto.Pair(
        product_name=product_name,
        category_name=category_name,
    )
