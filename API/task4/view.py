from fastapi import APIRouter
from .schemas import Response, Data
from .operations import isDecryptable

router = APIRouter(tags=["task4"])


@router.post("/", response_model=Response)
async def task3(parameters: Data):
    res, original, encoded, corrupted, decoded = isDecryptable(parameters.a, parameters.b, parameters.c)
    return Response(is_decrypted=res, original=original, encoded=encoded, corrupted=corrupted, decoded=decoded)
