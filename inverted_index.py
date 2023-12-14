import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import os
import pickle


def calculate_tfidf(documents):
    # Initialize the TF-IDF vectorizer
    vectorizer = TfidfVectorizer()

    # Fit and transform the documents
    tfidf_matrix = vectorizer.fit_transform(documents)

    return vectorizer, tfidf_matrix


def save_tfidf_matrix(matrix, output_dir, filename):
    output_file = os.path.join(output_dir, filename)
    with open(output_file, 'wb') as file:
        pickle.dump(matrix, file)


def load_tfidf_matrix(file_path):
    with open(file_path, 'rb') as file:
        loaded_matrix = pickle.load(file)
    return loaded_matrix


def display_matrix(matrix):
    # Convert the TF-IDF matrix to an array for display
    matrix_array = matrix.toarray()
    print("TF-IDF Matrix:")
    print(matrix_array)


def search_word_in_documents(word, vectorizer, tfidf_matrix):
    # Get the index of the word in the feature matrix
    word_index = vectorizer.vocabulary_.get(word)

    if word_index is not None:
        # Retrieve the TF-IDF vector for the given word
        word_vector = tfidf_matrix[:, word_index]

        # Find documents where the word appears with non-zero TF-IDF values
        non_zero_indices = word_vector.nonzero()[0]

        if len(non_zero_indices) > 0:
            print(f"The word '{word}' appears in the following document(s):")

            # Sort documents by their TF-IDF scores for the given word
            sorted_indices = np.argsort(-word_vector.toarray().flatten())  # Sort indices in descending order

            for index in sorted_indices:
                if word_vector[index] > 0:
                    print(f"Document {index + 1}: TF-IDF value = {word_vector[index, 0]}")
        else:
            print(f"The word '{word}' does not appear in any document.")
    else:
        print(f"The word '{word}' is not found in the documents.")


def inverted_main():
    input_dir = "stemming_output"  # Assuming preprocessed documents are stored here
    output_dir = "inverted_index"
    filename = "inverted_matrix.pkl"

    # Read preprocessed documents from the input directory
    documents = []
    for file_name in os.listdir(input_dir):
        if file_name.endswith(".sfx"):
            with open(os.path.join(input_dir, file_name), 'r') as file:
                documents.append(file.read())

    # Calculate TF-IDF
    vectorizer, tfidf_matrix = calculate_tfidf(documents)

    # Save TF-IDF matrix
    save_tfidf_matrix(tfidf_matrix, output_dir, filename)
    # Replace 'inverted_index' with your directory path where 'inverted_matrix.pkl' is stored
    file_path = os.path.join('inverted_index', 'inverted_matrix.pkl')

    # Load the TF-IDF matrix
    loaded_tfidf_matrix = load_tfidf_matrix(file_path)

    # Display the loaded TF-IDF matrix
    display_matrix(loaded_tfidf_matrix)
    # Assuming 'vectorizer' and 'loaded_tfidf_matrix' are already loaded or calculated
    # Replace 'word_to_search' with the word you want to search for in the documents
    while(True):
        word_to_search = input("Enter a word to search for: ")

        # Search for the word in the documents using the TF-IDF matrix and vectorizer
        search_word_in_documents(word_to_search, vectorizer, loaded_tfidf_matrix)


