from fastapi import FastAPI

from app.presentation.api.api import api_router
from app.presentation.api.healthcheck import healthcheck_router


def setup_controllers(app: FastAPI) -> None:
    app.include_router(api_router)
    app.include_router(healthcheck_router)
