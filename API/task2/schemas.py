from pydantic import BaseModel, ConfigDict
from typing import Annotated, List
from annotated_types import Ge, Le, Gt, MinLen


class Data(BaseModel):
    a: Annotated[int, Gt(0)]
    c: Annotated[int, Ge(0), Le(100)]
    b1: Annotated[int, Gt(0)]
    b2: Annotated[int, Gt(0)]


class ResponseBase(BaseModel):
    b: List[int]
    d: List[float]


class Response(ResponseBase):
    model_config = ConfigDict(from_attributes=True)