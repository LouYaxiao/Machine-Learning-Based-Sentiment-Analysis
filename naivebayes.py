import utils
import random
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from scipy.sparse import lil_matrix
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import csv

# Paths to your CSV files
TRAIN_PROCESSED_FILE = r"C:\Users\Lou13\Desktop\emotion_scores.csv"
TEST_PROCESSED_FILE = r"D:\大三上学期课程材料\大创\语料库\emotion_scores.csv"

# Feature Extraction Parameters
UNIGRAM_SIZE = 15000
USE_BIGRAMS = True
FEAT_TYPE = 'frequency'


# Function to process CSV and extract Word, Score pairs
def process_data(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header if any
        for row in reader:
            word, score = row[0], int(row[1])
            data.append((word, score))
    return data


# Function to extract features using CountVectorizer
def extract_features(words, use_bigrams=False):
    if use_bigrams:
        vectorizer = CountVectorizer(ngram_range=(1, 2), max_features=UNIGRAM_SIZE)
    else:
        vectorizer = CountVectorizer(max_features=UNIGRAM_SIZE)

    features = vectorizer.fit_transform(words)
    return features, vectorizer


# Function to apply TF-IDF transformation to feature matrix
def apply_tf_idf(X):
    transformer = TfidfTransformer(smooth_idf=True, sublinear_tf=True, use_idf=True)
    X_tfidf = transformer.fit_transform(X)
    return X_tfidf


if __name__ == '__main__':
    # Load training and test data
    train_data = process_data(TRAIN_PROCESSED_FILE)
    test_data = process_data(TEST_PROCESSED_FILE)

    # Separate words and scores for training
    train_words = [word for word, _ in train_data]
    train_scores = [score for _, score in train_data]

    # Separate words and scores for testing
    test_words = [word for word, _ in test_data]
    test_scores = [score for _, score in test_data]

    # Extract features from training data
    X_train, vectorizer = extract_features(train_words, use_bigrams=USE_BIGRAMS)

    # Apply TF-IDF transformation if required
    if FEAT_TYPE == 'frequency':
        X_train = apply_tf_idf(X_train)

    # Train the Naive Bayes model
    clf = MultinomialNB()
    clf.fit(X_train, train_scores)

    # Extract features from the test set using the same vectorizer
    X_test = vectorizer.transform(test_words)

    # Apply TF-IDF transformation to the test data
    if FEAT_TYPE == 'frequency':
        X_test = apply_tf_idf(X_test)

    # Make predictions on the test set
    predictions = clf.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(test_scores, predictions)
    print(f'Accuracy: {accuracy * 100:.2f}%')

    # Print some examples of correct/incorrect predictions
    for i in range(10):
        print(f'Word: {test_words[i]} | Actual: {test_scores[i]} | Predicted: {predictions[i]}')

