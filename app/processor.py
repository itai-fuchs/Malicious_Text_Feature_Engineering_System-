import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
# nltk.download('vader_lexicon')


class Processor:

    def __init__(self,collection):
        # convert the collection to df
        self.df= pd.DataFrame(collection)


#add a column that containing the rarest word in the record.
    def rare_word(self):
        if "Text" not in self.df.columns:
            raise ValueError("DataFrame must contain 'Text' column")
        rare_words = []
        for tweet in self.df["Text"]:
            words = pd.Series(tweet.lower().split())
            rarest_word = words.value_counts().idxmin() if not words.empty else None
            rare_words.append(rarest_word)
        self.df["rarest_word"] = rare_words

# analyzer the sentiment of the tweets
    def sentiment_intensity_analyzer(self):
        if "Text" not in self.df.columns:
            raise ValueError("DataFrame must contain 'Text' column")
        sentiment = []
        sia = SentimentIntensityAnalyzer()
        for tweet in self.df["Text"]:
            score = sia.polarity_scores(tweet)
            compound=score["compound"]
            if compound >= 0.5:
                sentiment.append("positive")
            elif compound <= -0.5:
                sentiment.append("negative")
            else:
                sentiment.append("neutral")

        self.df["SentimentIntensityAnalyzer"] = sentiment

    def find_weapon(self):
        if "Text" not in self.df.columns:
            raise ValueError("DataFrame must contain 'Text' column")

        with open("../data/weapon_list.txt", "r") as f:
            weapon_set = set(line.strip() for line in f)

        weapons = []
        for tweet in self.df["Text"]:
            found = None
            for word in tweet.split():
                if word in weapon_set:
                    found = word
                    break
            weapons.append(found)

        self.df["weapons_detected"] = weapons



