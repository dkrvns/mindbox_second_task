from di import bind_by_type, Container
from di.api.providers import DependencyProviderType
from di.api.scopes import Scope
from di.dependent import Dependent
from di.executors import AsyncExecutor
from didiator import Mediator, QueryMediator

from didiator.interface.utils.di_builder import DiBuilder
from didiator.utils.di_builder import DiBuilderImpl
from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker, AsyncSession

from app.application.interface.repository.category import CategoryRepository
from app.application.interface.repository.product import ProductRepository
from app.infra.db.main import build_sa_engine, build_sa_session_factory, build_sa_session
from app.infra.db.repository.category import CategoryRepositoryImpl
from app.infra.db.repository.product import ProductRepositoryImpl


def get_mediator() -> Mediator:
    raise NotImplemented


def init_di_builder() -> DiBuilder:
    di_container = Container()
    di_executor = AsyncExecutor()
    di_scopes = ["app", "request"]
    di_builder = DiBuilderImpl(di_container, di_executor, di_scopes=di_scopes)
    return di_builder


def setup_di_builder(di_builder: DiBuilder) -> None:
    di_builder.bind(
        bind_by_type(Dependent(lambda *args: di_builder, scope="app"), DiBuilder)
    )
    setup_mediator_factory(di_builder, get_mediator, "request")
    setup_db_factories(di_builder)


def setup_mediator_factory(
    di_builder: DiBuilder,
    mediator_factory: DependencyProviderType,
    scope: Scope,
) -> None:
    di_builder.bind(bind_by_type(Dependent(mediator_factory, scope=scope), Mediator))
    di_builder.bind(
        bind_by_type(Dependent(mediator_factory, scope=scope), QueryMediator)
    )


def setup_db_factories(di_builder: DiBuilder) -> None:
    di_builder.bind(bind_by_type(Dependent(build_sa_engine, scope="app"), AsyncEngine))
    di_builder.bind(
        bind_by_type(
            Dependent(build_sa_session_factory, scope="app"),
            async_sessionmaker[AsyncSession],
        ),
    )
    di_builder.bind(
        bind_by_type(Dependent(build_sa_session, scope="request"), AsyncSession)
    )
    di_builder.bind(
        bind_by_type(
            Dependent(CategoryRepositoryImpl, scope="request"),
            CategoryRepository,
            covariant=True,
        )
    )
    di_builder.bind(
        bind_by_type(
            Dependent(ProductRepositoryImpl, scope="request"),
            ProductRepository,
            covariant=True,
        )
    )
