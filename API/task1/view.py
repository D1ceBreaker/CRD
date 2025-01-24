from fastapi import APIRouter
from .schemas import Message, EncryptMessage
from .operation import encrypt_decrypt

router = APIRouter(tags=["task1"])


@router.post("/", response_model=Message)
async def task1(message_to_encrypt: EncryptMessage):
    message = message_to_encrypt.message
    n = message_to_encrypt.n
    c = message_to_encrypt.c

    decrypted: str = encrypt_decrypt(message, n, c)
    response: Message = Message(message=decrypted)
    return response

