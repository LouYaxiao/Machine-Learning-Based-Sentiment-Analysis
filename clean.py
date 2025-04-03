import win32com.client
import re

# Path to your document
doc_path = r"C:\Users\Lou13\Desktop\news_corpus2.txt"

def clean_text(text):
    # Use regex to remove non-letter characters
    return ' '.join(re.findall(r'\b[a-zA-Z]+\b', text))

def process_document(doc_path):
    # Initialize the Word application
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = False
    cleaned_content = []

    try:
        # Open the document
        doc = word.Documents.Open(doc_path)

        # Iterate through paragraphs in the document
        for para in doc.Paragraphs:
            cleaned_para = clean_text(para.Range.Text)
            if cleaned_para.strip():  # Only add non-empty cleaned paragraphs
                cleaned_content.append(cleaned_para)

    finally:
        # Close the document and Word application
        doc.Close(False)
        word.Quit()

    return cleaned_content

# Process the document
cleaned_corpus = process_document(doc_path)

# Optionally, save the cleaned content to a text file
with open(r"C:\Users\Lou13\Desktop\cleaned_corpus2.txt", "w", encoding="utf-8") as f:
    for line in cleaned_corpus:
        f.write(line + "\n")

print(f"Cleaned corpus created with {len(cleaned_corpus)} entries.")
