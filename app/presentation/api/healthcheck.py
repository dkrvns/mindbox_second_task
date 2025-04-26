from fastapi import APIRouter
from starlette import status

healthcheck_router = APIRouter(
    prefix="/healthcheck",
    tags=["healthcheck"],
)



@healthcheck_router.get("", status_code=status.HTTP_200_OK)
async def get_status() -> str:
    return 'ok'
