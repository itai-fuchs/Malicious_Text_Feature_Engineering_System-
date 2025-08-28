from fastapi import APIRouter, FastAPI
from dal import TweetRepository
import uvicorn
import logging
import traceback

logging.basicConfig(level=logging.ERROR)

router = APIRouter()
try:
    repo = TweetRepository()
except Exception as e:
    logging.error(f"Failed to initialize TweetRepository: {e}\n{traceback.format_exc()}")
    raise

@router.get("/")
def get_health():
    return {"Status": "🆗💯👍"}

@router.get("/tweets/antisemitic")
def get_antisemitic_tweets():
    try:
        return repo.get_tweets("antisemitic")
    except Exception as e:
        logging.error(f"Error in get_antisemitic_tweets: {e}\n{traceback.format_exc()}")
        raise

@router.get("/tweets/not_antisemitic")
def get_not_antisemitic_tweets():
    try:
        return repo.get_tweets("not_antisemitic")
    except Exception as e:
        logging.error(f"Error in get_not_antisemitic_tweets: {e}\n{traceback.format_exc()}")
        raise

app = FastAPI()
app.include_router(router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8008, reload=True)
