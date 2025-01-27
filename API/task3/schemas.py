from pydantic import BaseModel, ConfigDict
from typing import Annotated, List
from annotated_types import Ge, Le, Gt, MinLen


class Data(BaseModel):
    b: Annotated[int, Gt(0)]
    c: Annotated[int, Ge(0), Le(100)]
    a1: Annotated[int, Gt(0)]
    a2: Annotated[int, Gt(0)]


class ResponseBase(BaseModel):
    a: List[int]
    d: List[float]
    original: List[str]
    encoded: List[str]
    corrupted: List[str]
    decoded: List[str]
    batch: int


class Response(ResponseBase):
    model_config = ConfigDict(from_attributes=True)