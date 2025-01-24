from fastapi import APIRouter
from .schemas import Response, Data
from .operations import plot

router = APIRouter(tags=["task2"])


@router.post("/", response_model=Response)
async def task2(parameters: Data):
    b, d = plot(parameters.a, parameters.c, parameters.b1, parameters.b2)
    return Response(b=b, d=d)
