# NLP Corpus Manager
A simple command-line tool for managing and preprocessing text documents for NLP tasks.

---

## Features
- Store and manage text documents  
- Search documents by keywords  
- Preprocess text (Tokenization, Stopword Removal, Lemmatization, Word Frequency)  
- Load documents from a file  
- Export processed text to JSON  

---

## Installation & Usage
### Prerequisites
- Python 3.x (Check with `python --version` or `python3 --version`)
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

### Running the Application
#### Windows (CMD/PowerShell)
```bash
python main.py
```
#### Windows (Git Bash)
```bash
py main.py
```
#### Linux/macOS
```bash
python3 main.py
```

Type `'menu'` anytime to see available options.

---

## How to Load Documents from a File
1. Create a `.txt` file in this format:
   ```
   Title: AI Revolution
   AI is transforming industries worldwide.
   ```
2. Use **Option 7** in the menu to load from a file.

---

## License
This project is licensed under the MIT License.

---

## Next Steps
- Improve NLP preprocessing (stemming, named entity recognition, etc.)
- Build a GUI version
- Expand to support different text formats

---

