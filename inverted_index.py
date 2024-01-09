import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import os
import pickle

from TF_IDF import TFIDFCalculator


def calculate_tfidf(documents):
    # Initialize the TF-IDF vectorizer

    tfidf_calculator = TFIDFCalculator(directory="stemming_output")
    tfidf_matrix = tfidf_calculator.calculate_tfidf()
    print(tfidf_matrix)