from fastapi import APIRouter
from dal import TweetRepository
import uvicorn
from fastapi import FastAPI


router = APIRouter()
repo = TweetRepository()

@router.get("/")
def get_health():
    return {"Status" : "🆗💯👍"}


@router.get("/tweets/antisemitic")
def get_antisemitic_tweets():
    return repo.get_tweets("antisemitic")

@router.get("/tweets/not_antisemitic")
def get_not_antisemitic_tweets():
    return repo.get_tweets("not_antisemitic")



app = FastAPI()
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8008, reload=True)
