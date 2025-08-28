import re
import logging
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

logger = logging.getLogger(__name__)

nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

class TextProcessing:
    def __init__(self, text):
        self.real_text = text
        self.processed_text = text

    def comma_remover(self):
        try:
            self.processed_text = self.processed_text.replace(',', '')
        except Exception:
            logger.exception("Failed to remove commas from text.")

    def removes_special_characters(self):
        try:
            self.processed_text = re.sub(r'[^A-Za-z0-9.\s]', '', self.processed_text)
        except Exception:
            logger.exception("Failed to remove special characters from text.")

    def converts_to_lowercase(self):
        try:
            self.processed_text = self.processed_text.lower()
        except Exception:
            logger.exception("Failed to convert text to lowercase.")

    def removing_tabs(self):
        try:
            self.processed_text = re.sub(r'\s+', ' ', self.processed_text)
        except Exception:
            logger.exception("Failed to remove whitespace/tabs from text.")

    def removing_stop_words(self):
        try:
            words = self.processed_text.split()
            words = [w for w in words if w.lower() not in stopwords.words('english')]
            self.processed_text = " ".join(words)
        except Exception:
            logger.exception("Failed to remove stop words from text.")

    def finding_roots(self):
        try:
            lemmatizer = WordNetLemmatizer()
            words = self.processed_text.split()
            words = [lemmatizer.lemmatize(w, pos='v') for w in words]
            self.processed_text = " ".join(words)
        except Exception:
            logger.exception("Failed to lemmatize/find roots of words.")
