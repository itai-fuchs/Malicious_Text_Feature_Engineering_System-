from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI, COLLECTION, MONGO_DB



class Fetcher:
    def __init__(self):
        self.conn: AsyncIOMotorClient | None = None
        self.conf = MONGO_URI
        print("DB name:", self.conf)

    # Open connection
    def open_conn(self):
        if self.conn is None:
            self.conn = AsyncIOMotorClient(self.conf)
        return self.conn

    # get collection object
    def get_collection(self):
        conn = self.open_conn()
        db = conn[MONGO_DB]
        return db[COLLECTION]

    # read  the document of the collection
    async def read_collection(self):
        col = self.get_collection()
        docs = []
        async for d in col.find({}, {"_id": 0}):
            docs.append(d)
        return docs

    # close connection
    async def close_conn(self):
        if self.conn is not None:
            self.conn.close()
            self.conn = None


