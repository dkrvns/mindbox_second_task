from typing import Annotated

from didiator import QueryMediator
from fastapi import APIRouter, Depends

from app.application.commands.get_categories import GetCategories
from app.application.commands.get_pairs import GetPairs
from app.application.commands.get_products import GetProducts
from app.presentation.stub import Stub


api_router = APIRouter(
    prefix="/api",
)


@api_router.get("/products")
async def get_products(
    mediator: Annotated[QueryMediator, Depends(Stub(QueryMediator))],
):
    products = await mediator.query(
        GetProducts()
    )

    return products


@api_router.get("/categories")
async def get_categories(
    mediator: Annotated[QueryMediator, Depends(Stub(QueryMediator))],
):
    categories = await mediator.query(
        GetCategories()
    )

    return categories


@api_router.get("/pairs")
async def get_pairs(
    mediator: Annotated[QueryMediator, Depends(Stub(QueryMediator))],
):
    products = await mediator.query(
        GetProducts()
    )
    categories = await mediator.query(
        GetCategories()
    )
    pairs = await mediator.query(
        GetPairs(
            categories=categories,
            products=products,
        )
    )

    return pairs
