import asyncio
import logging

import uvicorn
from di import ScopeState
from didiator import Mediator
from didiator.interface.utils.di_builder import DiBuilder
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from app.infra.config_loader import load_config
from app.infra.di.main import init_di_builder, setup_di_builder
from app.infra.mediator.main import init_mediator, setup_mediator
from app.presentation.config import Config, setup_di_builder_config, APIConfig
from app.presentation.middleware.main import setup_middlewares
from app.presentation.provider.provider import setup_providers
from app.presentation.router.main import setup_controllers


def init_api(
    mediator: Mediator,
    di_builder: DiBuilder,
    di_state: ScopeState | None = None,
    debug: bool = __debug__,
) -> FastAPI:
    app = FastAPI(
        debug=debug,
        title="Test service",
        version="1.0.0",
        # default_response_class=ORJSONResponse,
    )
    setup_providers(app, mediator, di_builder, di_state)
    setup_middlewares(app)
    setup_controllers(app)
    return app


async def run_api(app: FastAPI, api_config: APIConfig) -> None:
    config = uvicorn.Config(
        app,
        host=api_config.host,
        port=api_config.port,
        log_level=logging.INFO,
        log_config=None,
    )
    server = uvicorn.Server(config)
    await server.serve()


async def main() -> None:
    config = load_config(Config)

    di_builder = init_di_builder()
    setup_di_builder(di_builder)
    setup_di_builder_config(di_builder, config)

    async with di_builder.enter_scope("app") as di_state:
        mediator = await di_builder.execute(init_mediator, "app", state=di_state)
        setup_mediator(mediator)

        app = init_api(mediator, di_builder, di_state, config.api.debug)
        await run_api(app, config.api)


if __name__ == "__main__":
    asyncio.run(main())
