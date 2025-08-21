from motor.motor_asyncio import AsyncIOMotorClient
from config import Config



class Fetcher:
    def __init__(self):
        self.conn: AsyncIOMotorClient | None = None
        self.conf = Config()

    # Open connection
    async def open_conn(self):
        if self.conn is None:
            self.conn = AsyncIOMotorClient(self.conf.MONGO_URI)
        return self.conn

    # get collection object
    def get_collection(self):
        conn = self.open_conn()
        return conn[self.conf.MONGO_DB][self.conf.COLLECTION]

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


