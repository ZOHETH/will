from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, JSON
from sqlalchemy.orm import relationship

from app.db import Base


class Item(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)


class TFModel(Base):
    name = Column(String(64), primary_key=True, index=True)
    type = Column(String(32), nullable=False)
    version = Column(Integer, default=-1, nullable=True)
    inputs_metadata = Column(JSON, nullable=True)
    extra = Column(JSON, default=dict)
