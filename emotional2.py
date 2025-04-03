import pandas as pd

# Load your emotionally biased words from the file
file_path = r"C:\Users\Lou13\Desktop\cleaned_corpus2.txt"

with open(file_path, 'r', encoding='utf-8') as file:
    words = [line.strip() for line in file.readlines()]

# Define a simple scoring system
# Adjust these lists according to your emotional bias classification
positive_words = [
            "Rich supplies", "Transparent process", "Sustainable debt management", "Independent study",
            "Positive outcome", "Essential to building consensus", "Greater equality", "Transcendental role",
            "Dignified lives", "Powerful", "Open", "Diverse", "Flexible", "Strategic", "Robust", "Sustainable",
            "Wealthy", "High quality", "Unique", "Alternative", "Fashionable"
    
            "Promote interests", "Highlight", "Mobilize funds", "Approved", "Showed", "Secured", "Strengthen",
            "Pressing for fair treatment", "Vowed", "Welcomed", "Help", "Strengthening", "Inject", "Spearhead",
            "Engaging", "Praise", "Reform", "Contribute", "Accelerated", "Donate"
       
            "Simply", "First and foremost", "Commonly", "Often", "Publicly expressed support", "Already",
            "Further", "Continually", "Effectively", "Ultimately", "Also", "Certainly"
       
            "Coalition", "Transparency", "Development", "Infrastructure", "Study", "Opportunities", "Vision",
            "Cooperation", "Investment", "Initiative", "Contributions", "Participation", "Solutions"
        ]  # Add your positive words
negative_words = [
            "Crippling financial crisis", "Impoverished countries", "Protracted debt overhauls", "High risk",
            "Battered by extreme weather", "Shrinking", "Dwindling", "Rapidly aging", "Criticized", "Adverse",
            "Cheap", "Fleeting", "Poor", "Detrimental", "Fast in fast fashion"
       
            "Fret about", "Struggle to repay", "Killing each other", "Gloss over", "Accuse", "Scavenges",
            "Undermine", "Phase out", "Expelled", "Blame"
       
            "Significantly delayed", "Most likely represent a strategy", "Expectedly", "Tremendously",
            "Not necessarily"
       
            "Crisis", "Burdens", "Disparities", "Pressure", "Criticism", "Consequences", "Overconsumption",
            "Resistance", "Vulnerability", "Power dynamics", "Colonial histories"
        ]           # Add your neutral words
neutral_words =  [
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
        ]    # Add your negative words

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