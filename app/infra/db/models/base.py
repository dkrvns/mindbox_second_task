import datetime
from sqlalchemy import MetaData, sql
from sqlalchemy.orm import DeclarativeBase, registry
from sqlalchemy.orm import Mapped, mapped_column


mapper_registry = registry(metadata=MetaData())


class BaseModel(DeclarativeBase):
    registry = mapper_registry
    metadata = mapper_registry.metadata

