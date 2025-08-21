from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from app.fetcher import Fetcher
from app.manager import Manager


fetch = Fetcher()


@asynccontextmanager
async def lifespan(app: FastAPI):
    fetch.open_conn()
    yield
    await fetch.close_conn()

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def health():
    return {"status": "ok"}

@app.get("/data")
async def get_data():
    return await Manager.flow_chart()



if "__main__" == __name__:
    uvicorn.run(app, host="127.0.0.1", port=8000)