from nltk.sentiment.vader import SentimentIntensityAnalyzer as sia
from Preprocessor.utils import process_text
import re
from datetime import datetime

class Enricher:

    def __init__(self,text):
        self.text=text

    def sentiment_analyzer(self):
            score = sia.polarity_scores(self.text)
            compound = score["compound"]
            if compound >= 0.5:
                sentiment="positive"
            elif compound <= -0.5:
                sentiment="negative"
            else:
                sentiment="neutral"
            return sentiment


    def find_weapon(self):
        weapons_list=[]
        with open("weapon_list.txt", "r") as f:
           weapon_set = set(process_text(f.read()).split())
           for word in self.text.split():
                if word in weapon_set:
                    weapons_list.append(word)

        return weapons_list

    def latest_timestamp(self):
        matches = re.findall(r"\d{4}-\d{2}-\d{2}(?: \d{2}:\d{2}(?::\d{2})?)?", self.text)
        if not matches:
            return None
        dates = [datetime.fromisoformat(m) for m in matches]
        return max(dates).isoformat(sep=" ")

