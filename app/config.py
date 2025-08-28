import os

MONGO_DB   = os.getenv("MONGO_DB", "IranMalDB")
MONGO_USER = os.getenv("MONGO_USER", "IRGC_NEW")
MONGO_PASS = os.getenv("MONGO_PASS", "iran135")
MONGO_HOST = os.getenv("MONGO_HOST", "cluster0.6ycjkak.mongodb.net/")


MONGO_URI = os.getenv(
    "MONGO_URI",
    f"mongodb+srv://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}{MONGO_DB}?retryWrites=true&w=majority"
)

COLLECTION = os.getenv("MONGO_COLLECTION", "tweets")




