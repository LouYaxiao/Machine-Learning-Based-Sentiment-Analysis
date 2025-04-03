import pandas as pd

# Load your emotionally biased words from the file
file_path = r"C:\Users\Lou13\Desktop\cleaned_corpus.txt"

# Read the file
with open(file_path, 'r', encoding='utf-8') as file:
    words = [line.strip() for line in file.readlines()]

# Define a simple scoring system
# Adjust these lists according to your emotional bias classification
positive_words = [
        "important", "successful", "sustainable", "good", "great", "mutual",
        "active", "special", "global", "glorious", "commendable", "immense",
        "phenomenal", "strategic", "firm", "economic", "social", "grateful",
        "efficient", "clean", "meaningful", "strong", "significant", "high quality",
        "betterment", "green", "enhanced", "sincere", "remarkable", "help",
        "promote", "encourage", "celebrate"
    ]  # Add your positive words
negative_words = [
        "anti-Western", "complex", "maligned", "poor", "daunting",
        "devastating", "exclusive", "inequalities", "poverty",
        "destroy", "deny", "tackle"
    ]           # Add your neutral words
neutral_words = [
        "senior", "solid", "warm", "historical", "common", "developing",
        "top", "long term", "unified", "structured", "huge", "key",
        "bilateral", "political", "roles", "capacity", "trade",
        "mechanism", "population", "strategies"
    ]     # Add your negative words

# Initialize scores dictionary
word_scores = {}

# Assign scores based on emotional bias
for word in words:
    if word in positive_words:
        word_scores[word] = 1  # Positive score
    elif word in neutral_words:
        word_scores[word] = 0  # Neutral score
    elif word in negative_words:
        word_scores[word] = -1  # Negative score
    else:
        word_scores[word] = 0  # Default to neutral if not found

# Convert to DataFrame for better visualization
scores_df = pd.DataFrame(word_scores.items(), columns=['Word', 'Score'])

# Save the scores to a new file
output_path = r"C:\Users\Lou13\Desktop\emotion_scores.csv"
scores_df.to_csv(output_path, index=False)

print("Sentiment scores assigned and saved to emotion_scores.csv.")
