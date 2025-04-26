from didiator import Mediator, QueryDispatcherImpl, MediatorImpl
from didiator.interface.utils.di_builder import DiBuilder
from didiator.middlewares.di import DiMiddleware, DiScopes
from didiator.middlewares.logging import LoggingMiddleware

from app.application.commands.get_categories import GetCategories, GetCategoriesHandler
from app.application.commands.get_products import GetProducts, GetProductsHandler
from app.application.commands.get_pairs import GetPairs, GetPairsHandler


def init_mediator(di_builder: DiBuilder) -> Mediator:
    middlewares = (
        LoggingMiddleware("mediator"),
        DiMiddleware(di_builder, scopes=DiScopes("request")),
    )
    query_dispatcher = QueryDispatcherImpl(middlewares=middlewares)

    mediator = MediatorImpl(query_dispatcher=query_dispatcher)
    return mediator

def setup_mediator(mediator: Mediator) -> None:
    mediator.register_query_handler(GetProducts, GetProductsHandler)
    mediator.register_query_handler(GetCategories, GetCategoriesHandler)
    mediator.register_query_handler(GetPairs, GetPairsHandler)
