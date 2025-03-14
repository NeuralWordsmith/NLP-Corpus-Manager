import sys
from corpus import Corpus

def display_menu():
    """Displays the interactive CLI menu."""
    print("\n========================================")
    print("📜 NLP Corpus Manager".center(40))
    print("========================================")
    print("1. Add Document")
    print("2. List Documents")
    print("3. Search Documents")
    print("4. Preprocess Corpus")
    print("5. Export Corpus")
    print("6. Delete a Document")
    print("7. Load Document from File")
    print("8. Exit")
    print("========================================")

def main():
    corpus = Corpus()
    stopwords = {"the", "is", "and", "in", "on", "at"}  # Example stopwords

    print("\n📜 NLP Corpus Manager - Type 'menu' to view options")
    display_menu()  # Show menu once at startup

    while True:
        choice = input("\nEnter your choice (or 'menu' to show options): ").strip()

        if choice.lower() == "menu":
            display_menu()
            continue

        if not choice.isdigit():
            print("⚠ Invalid choice! Please enter a number between 1-8.")
            continue

        choice = int(choice)

        if choice == 1:
            title = input("Enter document title: ")
            content = input("Enter document content: ")
            corpus.add_document(title, content)
            print(f"✅ Document '{title}' added.")

        elif choice == 2:
            docs = corpus.list_documents()
            if docs:
                print("📄 Available Documents:", docs)
            else:
                print("⚠ No documents found.")

        elif choice == 3:
            keyword = input("Enter keyword to search: ")
            results = corpus.search_documents(keyword)
            if results:
                print(f"🔍 Documents containing '{keyword}': {results}")
            else:
                print("⚠ No documents found.")

        elif choice == 4:
            corpus.preprocess_corpus(stopwords)
            print("✅ Corpus preprocessing completed.")

        elif choice == 5:
            corpus.export_corpus("corpus.json")
            print("✅ Corpus exported successfully.")

        elif choice == 6:
            doc_title = input("Enter document title to delete: ")
            if doc_title in corpus.list_documents():
                corpus.documents = [doc for doc in corpus.documents if doc.title != doc_title]
                corpus.save_corpus()
                print(f"🗑 Document '{doc_title}' deleted.")
            else:
                print("⚠ Document not found.")

        elif choice == 7:
            file_path = input("Enter the path to the text file: ").strip()
            corpus.add_document_from_file(file_path)

        elif choice == 8:
            print("👋 Exiting NLP Corpus Manager. Goodbye!")
            sys.exit()

        else:
            print("⚠ Invalid choice! Please enter a number between 1-8.")

        choice = int(choice)

if __name__ == "__main__":
    main()
