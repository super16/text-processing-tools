from pydantic import dataclasses
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass


class Base(
    MappedAsDataclass,
    DeclarativeBase,
    dataclass_callable=dataclasses.dataclass,
):
    pass
