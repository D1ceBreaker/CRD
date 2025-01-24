from fastapi import APIRouter
from .schemas import Response, Data
from .operations import isDecryptable

router = APIRouter(tags=["task4"])


@router.post("/", response_model=Response)
async def task3(parameters: Data):
    res = isDecryptable(parameters.a, parameters.b, parameters.c)
    return Response(is_decrypted=res)
