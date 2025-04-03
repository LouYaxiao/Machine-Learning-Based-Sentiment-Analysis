import pandas as pd
import win32com.client as win32

# Load the sentiment scores from the CSV file
scores_file_path = r"C:\Users\Lou13\Desktop\emotion_scores2.csv"
scores_df = pd.read_csv(scores_file_path)
scores_dict = dict(zip(scores_df['Word'], scores_df['Score']))

# Function to analyze the sentiment of a speech segment
def analyze_sentiment(segment):
    words = segment.split()  # Tokenize the segment into words
    total_score = sum(scores_dict.get(word, 0) for word in words)  # Sum scores
    return total_score

# Load the speech segments from the DOC file using pywin32
doc_file_path = r"C:\Users\Lou13\Desktop\USnews新闻内容.docx"
word = win32.gencache.EnsureDispatch('Word.Application')
doc = word.Documents.Open(doc_file_path)

# Analyze sentiment for each paragraph (or segment)
results = []
for i, para in enumerate(doc.Paragraphs):
    text = para.Range.Text.strip()  # Get the text of the paragraph
    if text:  # Ignore empty paragraphs
        sentiment_score = analyze_sentiment(text)
        results.append((f'Paragraph {i+1}: {text}', sentiment_score))

# Clean up
doc.Close(False)  # Close the document without saving
word.Quit()  # Quit Word application

# Convert results to DataFrame for better visualization
results_df = pd.DataFrame(results, columns=['Segment', 'Sentiment Score'])

# Save the results to a new file
output_path = r"C:\Users\Lou13\Desktop\sentiment_analysis_results2.csv"
results_df.to_csv(output_path, index=False)

print("Sentiment analysis completed and saved to sentiment_analysis_results2.csv.")
