import re
import nltk
from collections import Counter
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Download resources
nltk.download('wordnet')
nltk.download('omw-1.4')

class Document:
    """Represents a single text document."""

    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.tokens = []
        self.word_freq = {}
        self.stemmed_tokens = []
        self.lemmatized_tokens = []
        self.stemmer = PorterStemmer()
        self.lemmatizer = WordNetLemmatizer()

    def tokenize(self):
        """Splits text into words and stores tokens."""
        self.tokens = re.findall(r'\b\w+\b', self.content.lower())

    def remove_stopwords(self, stopwords):
        """Removes stopwords from tokens."""
        self.tokens = [word for word in self.tokens if word not in stopwords]

    def compute_word_frequency(self):
        """Counts the frequency of each word."""
        self.word_freq = dict(Counter(self.tokens))

    def stem_words(self):
        """Applies stemming to tokens."""
        self.stemmed_tokens = [self.stemmer.stem(word) for word in self.tokens]

    def lemmatize_words(self):
        """Applies lemmatization to tokens."""
        self.lemmatized_tokens = [self.lemmatizer.lemmatize(word) for word in self.tokens]

    def document_statistics(self):
        """Returns basic statistics about the document."""
        total_words = len(self.tokens)
        unique_words = len(set(self.tokens))
        avg_word_length = sum(len(word) for word in self.tokens) / total_words if total_words > 0 else 0
        top_words = dict(sorted(self.word_freq.items(), key=lambda x: x[1], reverse=True)[:5])  # Top 5 words

        return {
            "Total Words": total_words,
            "Unique Words": unique_words,
            "Average Word Length": round(avg_word_length, 2),
            "Top Words": top_words
        }

# Example usage
if __name__ == "__main__":
    stopwords = {"the", "is", "and", "in", "on", "at"}
    doc = Document("Sample", "The quick brown fox jumps over the lazy dog running in the park. The dog is fast.")

    doc.tokenize()
    doc.remove_stopwords(stopwords)
    doc.compute_word_frequency()
    doc.stem_words()
    doc.lemmatize_words()

    stats = doc.document_statistics()

    print("Tokens:", doc.tokens)
    print("Word Frequency:", doc.word_freq)
    print("Stemmed Tokens:", doc.stemmed_tokens)
    print("Lemmatized Tokens:", doc.lemmatized_tokens)
    print("\n📊 Document Statistics:", stats)
