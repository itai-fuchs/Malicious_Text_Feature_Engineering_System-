from app.processor import Processor
from fetcher import Fetcher




class Manager:

    @staticmethod
    async def flow_chart():
        fetcher = Fetcher()
        collection = await fetcher.read_collection()
        await fetcher.close_conn()

        processor = Processor(collection)
        processor.rare_word()
        processor.sentiment_intensity_analyzer()
        processor.find_weapon()

        return processor.df.to_dict(orient="records")


import asyncio

async def main():
    data = await Manager.flow_chart()
    print(data[0])

asyncio.run(main())
