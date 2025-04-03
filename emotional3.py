import pandas as pd

# Load your emotionally biased words from the file
file_path = r"C:\Users\Lou13\Desktop\filtered_corpus_word_list2.txt"

# Read the words from the main corpus file
with open(file_path, 'r', encoding='utf-8') as file:
    words = [line.strip() for line in file.readlines()]

# Load positive and negative words from separate files
positive_words_path = r"C:\Users\Lou13\Desktop\sentiment-analysis\positive-words.txt"
negative_words_path = r"C:\Users\Lou13\Desktop\sentiment-analysis\negative-words.txt"

# Read the positive words file
with open(positive_words_path, 'r', encoding='utf-8') as pos_file:
    positive_words = [line.strip() for line in pos_file.readlines()]

# Read the negative words file
with open(negative_words_path, 'r', encoding='utf-8') as neg_file:
    negative_words = [line.strip() for line in neg_file.readlines()]

# Define some neutral words manually or load them from a file if needed
neutral_words = [
    "Complicated", "Developing countries", "Notable absentees", "Critical minerals", "Uneven nature",
            "Asymmetric loans", "Vastly different", "Divergent foreign policy goals", "Major", "Comprehensive",
            "Key", "Increasing", "High risk", "Alternative"
        
            "Depends upon", "Considered", "Host a summit", "Use different criteria", "Gain traction", "Speculated",
            "Review", "Marked", "Curb risks", "Looking for a sustainable level", "Pushing", "Agree on mechanisms",
            "Adopted", "Address issues", "Aims", "Consumed", "Discard"
        
            "Not regularly used", "Currently", "Rapidly", "Now includes", "Eventually"
        
            "Term", "Countries", "Definition", "Criteria", "Population", "Influence", "Agenda", "Negotiations",
            "Loans", "Economies", "Cash", "Projects", "Finance", "Climate change", "Technology", "Summit",
            "Ambition", "Relations", "Security", "Ideologies", "Principles", "Gaps", "Practices", "Mindset",
            "Market demands"
]

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
output_path = r"C:\Users\Lou13\Desktop\emotion_scores2.csv"
scores_df.to_csv(output_path, index=False)

print("Sentiment scores assigned and saved to emotion_scores.csv.")
