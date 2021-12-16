from typing import Any
import re

from sqlalchemy.ext.declarative import as_declarative, declared_attr


def hump2underline(hump_str):
    p = re.compile(r'([a-z]|\d)([A-Z])')
    sub = re.sub(p, r'\1_\2', hump_str).lower()
    return sub


@as_declarative()
class Base:
    id: Any
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return hump2underline(cls.__name__)
