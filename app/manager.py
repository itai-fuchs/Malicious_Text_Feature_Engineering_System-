from processor import Processor
from fetcher import Fetcher




class Manager:

    @staticmethod
    async def flow_chart():
        fetcher = Fetcher()
        collection = await fetcher.read_collection()


        processor = Processor(collection)
        processor.rare_word()
        processor.sentiment_intensity_analyzer()
        processor.find_weapon()

        return processor.df.to_dict(orient="records")


