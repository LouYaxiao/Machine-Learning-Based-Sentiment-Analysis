import win32com.client

# Path to your document
doc_path = r"C:\Users\Lou13\Desktop\USnews新闻内容.docx"

def create_corpus(doc_path):
    # Initialize the Word application
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = False
    corpus = []

    try:
        # Open the document
        doc = word.Documents.Open(doc_path)

        # Iterate through paragraphs in the document
        for para in doc.Paragraphs:
            if para.Range.Text.strip():  # Only add non-empty paragraphs
                corpus.append(para.Range.Text.strip())

    finally:
        # Ensure the document and Word application are properly closed
        if 'doc' in locals() and doc:
            doc.Close(False)
        if 'word' in locals() and word:
            word.Quit()

    return corpus

# Create the corpus
news_corpus = create_corpus(doc_path)

# Optionally, save the corpus to a text file
with open(r"C:\Users\Lou13\Desktop\news_corpus2.txt", "w", encoding="utf-8") as f:
    for news in news_corpus:
        f.write(news + "\n")

print(f"Corpus created with {len(news_corpus)} entries.")



