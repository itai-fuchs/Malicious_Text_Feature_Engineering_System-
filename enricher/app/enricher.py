from nltk.sentiment.vader import SentimentIntensityAnalyzer as sia
import nltk
nltk.download('vader_lexicon',quiet=True)
from Preprocessor.utils import process_text
from datetime import datetime
import config
import logging


logger = logging.getLogger(__name__)


class Enricher:


    """
           Analyze the sentiment of the text using VADER.
    """
    @staticmethod
    def sentiment_analyzer(text):
        try:
            score = sia().polarity_scores(text)
            compound = score["compound"]
            if compound >= 0.5:
                sentiment = "positive"
            elif compound <= -0.5:
                sentiment = "negative"
            else:
                sentiment = "neutral"
            return sentiment
        except Exception as e:
            logger.error(f"Error analyzing sentiment: {e}")
            return None

    """
     Find words in the text that match entries in the weapon list.
        
    """

    @staticmethod
    def find_weapon(text):
        try:
            weapons_list = []
            with open(config.data_path, "r") as f:
                weapon_set = set(process_text(f.read()).split())
                for word in text.split():
                    if word in weapon_set:
                        weapons_list.append(word)
            return weapons_list
        except FileNotFoundError:
            logger.error(f"Weapon list file not found: {data_path}")
            return None

    """
    Extract the latest timestamp from the text.
        
    """
    @staticmethod
    def latest_timestamp(text):
        try:
            import re

            matches = re.findall(r"\d{4}-\d{2}-\d{2}",text)

            if not matches:
                return None
            dates = [datetime.fromisoformat(m) for m in matches]
            return max(dates).isoformat(sep=" ")
        except Exception as e:
            logger.error(f"Error extracting latest timestamp: {e}")
            return None
