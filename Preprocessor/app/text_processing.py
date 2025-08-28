import re
import nltk
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

class TextProcessing:
    def __init__(self, text):
        self.real_text = text
        self.processed_text = text

    # Removing punctuation marks
    def comma_remover(self):
        self.processed_text = self.processed_text.replace(',', '')

    # Removing special characters
    def removes_special_characters(self):
        self.processed_text = re.sub(r'[^A-Za-z0-9.\s]', '', self.processed_text)

    # Convert text to lowercase
    def converts_to_lowercase(self):
        self.processed_text = self.processed_text.lower()

    # Removing unnecessary whitespace
    def removing_tabs(self):
        self.processed_text = re.sub(r'\s+', ' ', self.processed_text)

    # Removing stop words
    def removing_stop_words(self):
        words  = self.processed_text.split()
        words = [w for w in words if w.lower() not in stopwords.words('english')]
        self.processed_text = " ".join(words)

    # Metathesis (finding roots)
    def finding_roots(self):
        lemmatizer = WordNetLemmatizer()
        words = self.processed_text.split()
        words = [lemmatizer.lemmatize(w, pos='v') for w in words]
        self.processed_text = " ".join(words)


