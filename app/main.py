from fastapi import FastAPI
from contextlib import asynccontextmanager
from manager import Manager
from fetcher import Fetcher
fetcher=Fetcher()
manager=Manager()

@asynccontextmanager
async def lifespan(app: FastAPI):

    await fetcher.open_conn()
    yield

    await manager.close_conn()

app = FastAPI(lifespan=lifespan)

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/data")
async def get_data():
    return await manager.flow_chart()
