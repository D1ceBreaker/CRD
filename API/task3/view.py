from fastapi import APIRouter
from .schemas import Response, Data
from .operations import plot

router3 = APIRouter(tags=["task3"])


@router3.post("/", response_model=Response)
async def task3(parameters: Data):
    a, d = plot(parameters.a1, parameters.a2, parameters.b, parameters.c)
    return Response(a=a, d=d)
