from pydantic import BaseModel, ConfigDict
from typing import Annotated
from annotated_types import Ge, Le, Gt, MinLen


class MessageBase(BaseModel):
    message: Annotated[str, MinLen(1)]


class EncryptMessage(MessageBase):
    n: Annotated[int, Gt(0)]
    c: Annotated[int, Ge(0), Le(100)]


class Message(MessageBase):
    model_config = ConfigDict(from_attributes=True)

