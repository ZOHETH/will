from pydantic import BaseModel


class Item(BaseModel):
    id: int

    class Config:
        orm_mode = True


class TFModel(BaseModel):
    name: str
    type: str
    version: int
    inputs_metadata: dict
    extra: dict

    class Config:
        orm_mode = True
