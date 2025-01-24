from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn


from API.task1.view import router as task1_router
from API.task2.view import router as task2_router
from API.task3.view import router3 as task3_router
from API.task4.view import router as task4_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router=task1_router, prefix="/task1")
app.include_router(router=task2_router, prefix="/task2")
app.include_router(router=task3_router, prefix="/task3")
app.include_router(router=task4_router, prefix="/task4")

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)