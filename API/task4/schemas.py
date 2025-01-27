from pydantic import BaseModel, ConfigDict
from typing import Annotated, List
from annotated_types import Ge, Le, Gt, MinLen


class Data(BaseModel):
    a: Annotated[int, Gt(0)]
    b: Annotated[int, Gt(0)]
    c: Annotated[int, Ge(0), Le(100)]


class ResponseBase(BaseModel):
    is_decrypted: bool
    original: str
    encoded: str
    corrupted: str
    decoded: str


class Response(ResponseBase):
    model_config = ConfigDict(from_attributes=True)
