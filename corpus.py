import json
import os
from document import Document

class Corpus:
    """Manages a collection of text documents with persistence."""

    def __init__(self, filename="corpus.json"):
        self.documents = []
        self.filename = filename
        self.load_corpus()  # Load corpus on startup

    def add_document(self, title, content):
        """Creates a Document object and adds it to the corpus."""
        doc = Document(title, content)
        self.documents.append(doc)
        self.save_corpus()

    def list_documents(self):
        """Lists all document titles in the corpus."""
        return [doc.title for doc in self.documents]

    def search_documents(self, keyword):
        """Searches documents by keyword."""
        return [doc.title for doc in self.documents if keyword.lower() in doc.content.lower()]

    def preprocess_corpus(self, stopwords):
        """Applies tokenization, stopword removal, and word frequency computation to all documents."""
        for doc in self.documents:
            doc.tokenize()
            doc.remove_stopwords(stopwords)
            doc.compute_word_frequency()
        self.save_corpus()

    def save_corpus(self):
        """Saves corpus data to a JSON file."""
        corpus_data = {
            doc.title: {"content": doc.content, "tokens": doc.tokens, "word_freq": doc.word_freq}
            for doc in self.documents
        }
        with open(self.filename, "w") as f:
            json.dump(corpus_data, f, indent=4)
        print(f"✅ Corpus saved to {self.filename}")

    def load_corpus(self):
        """Loads documents from a JSON file if it exists and has the correct structure."""
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                corpus_data = json.load(f)

            for title, data in corpus_data.items():
                if "content" in data:  # Ensure the key exists
                    doc = Document(title, data["content"])
                    doc.tokens = data.get("tokens", [])  # Handle missing keys safely
                    doc.word_freq = data.get("word_freq", {})
                    self.documents.append(doc)

            print(f"✅ Corpus loaded from {self.filename}")
        else:
            print("⚠️ No previous corpus found. Starting fresh.")

    def export_corpus(self, filename="corpus.json"):
        """Saves processed corpus data to a JSON file."""
        corpus_data = {
            doc.title: {
                "content": doc.content,
                "tokens": doc.tokens,
                "word_freq": doc.word_freq
            }
            for doc in self.documents
        }
        with open(filename, "w") as f:
            json.dump(corpus_data, f, indent=4)
        print(f"✅ Corpus exported to {filename}")

    def add_document_from_file(self, file_path):
        """Loads a document from a text file and adds it to the corpus, preventing duplicates."""
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                lines = [line.strip() for line in file.readlines() if line.strip()]

            print("📂 File contents ->", lines)  # Debugging output

            if len(lines) < 2:
                print("⚠ Invalid file format. Ensure the first line is the title and the rest is content.")
                return

            if lines[0].lower().startswith("title:"):
                title = lines[0][7:].strip()
            else:
                print("⚠ Invalid format. First line must start with 'Title: '")
                return

            content = " ".join(lines[1:])

            # 🔹 Check if the document already exists before adding
            if any(doc.title == title for doc in self.documents):
                print(f"⚠ Document '{title}' already exists. Skipping duplicate entry.")
                return

            self.add_document(title, content)
            print(f"✅ Document '{title}' added from {file_path}")

        except FileNotFoundError:
            print(f"⚠ File '{file_path}' not found.")

        except Exception as e:
            print(f"⚠ Error loading file: {e}")

# Example usage
if __name__ == "__main__":
    stopwords = {"the", "is", "and", "in", "on", "at"}
    corpus = Corpus()

    # Adding sample documents
    corpus.add_document("Doc 1", "The quick brown fox jumps over the lazy dog.")
    corpus.add_document("Doc 2", "Natural Language Processing is a fascinating field of AI.")

    print("📄 Available Documents:", corpus.list_documents())

    # Preprocessing corpus
    corpus.preprocess_corpus(stopwords)

