import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


def calculate_tfidf(directory):
    files = [file for file in os.listdir(directory) if file.endswith('.sfx')]

    file_texts = []
    file_names = []

    # Read the files and store their contents and names
    for file in files:
        with open(os.path.join(directory, file), 'r', encoding='utf-8') as f:
            file_texts.append(f.read())
            file_names.append(file)

    # Initialize the TfidfVectorizer
    vectorizer = TfidfVectorizer(use_idf=True)

    # Calculate TF-IDF
    tfidf_matrix = vectorizer.fit_transform(file_texts)

    # Create a DataFrame to display the results
    tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out(), index=file_names)

    # Print the TF-IDF results in a clean table format
    print(tfidf_df)


if __name__ == '__main__':
    calculate_tfidf(directory="stemming_output")