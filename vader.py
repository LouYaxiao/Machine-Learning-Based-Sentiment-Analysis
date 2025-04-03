import codecs
import os
from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))
def read(*parts):
    """
    Build an absolute path from *parts* and and return the contents of the
    resulting file.  Assume UTF-8 encoding.
    """
    with codecs.open(os.path.join(HERE, *parts), "rb", "utf-8") as f:
        return f.read()

setup(
  name = 'vaderSentiment',
  #packages = ['vaderSentiment'], # this must be the same as the name above
  packages = find_packages(exclude=['tests*']), # a better way to do it than the line above -- this way no typo/transpo errors
  include_package_data=True,
  version = '3.3.1',
  description = 'VADER Sentiment Analysis. VADER (Valence Aware Dictionary and sEntiment Reasoner) is a lexicon and rule-based sentiment analysis tool that is specifically attuned to sentiments expressed in social media, and works well on texts from other domains.',
  long_description = read("README.rst"),
  long_description_content_type = 'text/x-rst',
  author = 'C.J. Hutto',
  author_email = 'cjhutto@gatech.edu',
  license = 'MIT License: http://opensource.org/licenses/MIT',
  url = 'https://github.com/cjhutto/vaderSentiment', # use the URL to the github repo
  download_url = 'https://github.com/cjhutto/vaderSentiment/archive/master.zip',
  install_requires = ['requests'],
  keywords = ['vader', 'sentiment', 'analysis', 'opinion', 'mining', 'nlp', 'text', 'data',
              'text analysis', 'opinion analysis', 'sentiment analysis', 'text mining', 'twitter sentiment',
              'opinion mining', 'social media', 'twitter', 'social', 'media'], # arbitrary keywords
  classifiers = ['Development Status :: 4 - Beta', 'Intended Audience :: Science/Research',
                 'License :: OSI Approved :: MIT License', 'Natural Language :: English',
                 'Programming Language :: Python :: 3.5', 'Topic :: Scientific/Engineering :: Artificial Intelligence',
                 'Topic :: Scientific/Engineering :: Information Analysis', 'Topic :: Text Processing :: Linguistic',
                 'Topic :: Text Processing :: General'],
)

import os
from nltk import tokenize
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import docx  # Library to read .docx files
import csv  # Library to write to CSV


def read_docx(file_path):
    """Reads text from a .docx file."""
    doc = docx.Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return "\n".join(full_text)


def sentiment(text):
    """Analyzes the sentiment of a given text using VADER."""
    analyzer = SentimentIntensityAnalyzer()
    return analyzer.polarity_scores(text)


if __name__ == '__main__':
    # Initialize sentences as a list to store the tokenized sentences
    sentences = []

    # File path to the .docx document
    file_path = r"C:\Users\Lou13\Desktop\training\news from cgtn.docx"

    # Read the content from the .docx file
    docx_content = read_docx(file_path)

    # Tokenize the content into sentences
    lines_list = tokenize.sent_tokenize(docx_content)

    # Extend the 'sentences' list with tokenized sentences from the .docx content
    sentences.extend(lines_list)

    # Define the output CSV file path
    output_csv_path = os.path.join(os.path.dirname(file_path), 'sentiment_analysis_output.csv')

    # Perform sentiment analysis on each sentence and write results to a CSV file
    with open(output_csv_path, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Sentence', 'Negative', 'Neutral', 'Positive', 'Compound'])

        for sentence in sentences:
            ss = sentiment(sentence)
            writer.writerow([sentence, ss['neg'], ss['neu'], ss['pos'], ss['compound']])

    print(f"Sentiment analysis results saved to {output_csv_path}")
