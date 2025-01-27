from fastapi import APIRouter
from .schemas import Response, Data
from .operations import plot

router3 = APIRouter(tags=["task3"])


@router3.post("/", response_model=Response)
async def task3(parameters: Data):
    a, d, original, encoded, corrupted, decoded, batch = plot(parameters.a1, parameters.a2, parameters.b, parameters.c)
    return Response(a=a, d=d, original=original, encoded=encoded, corrupted=corrupted, decoded=decoded, batch=batch)
