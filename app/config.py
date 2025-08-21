import os

class Config:
    def __init__(self):
        self.MONGO_DB   = os.getenv("MONGO_DB", "IranMalDB")
        self.MONGO_USER = os.getenv("MONGO_USER", "IRGC")
        self.MONGO_PASS = os.getenv("MONGO_PASS", "iraniraniran")
        self.MONGO_HOST = os.getenv("MONGO_HOST", "iranmaldb.gurutam.mongodb.net")


        self.MONGO_URI = os.getenv(
            "MONGO_URI",
            f"mongodb+srv://{self.MONGO_USER}:{self.MONGO_PASS}@{self.MONGO_HOST}/{self.MONGO_DB}?retryWrites=true&w=majority"
        )

        self.COLLECTION = os.getenv("MONGO_COLLECTION", "tweets")




