import os
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from tabulate import tabulate


# Function to read documents from a directory
def read_documents_from_directory(directory):
    documents = []
    file_names = []
    for filename in os.listdir(directory):
        if filename.endswith(".sfx"):
            with open(os.path.join(directory, filename), 'r') as file:
                content = file.read()
                documents.append(content)
                file_names.append(os.path.splitext(filename)[0])  # Save file names without extension
    return documents, file_names


def inverted_boolean():
    # Directory containing .sfx documents
    input_directory = "stemming_output"

    # Read documents and get file names
    documents, file_names = read_documents_from_directory(input_directory)

    # Create CountVectorizer with binary=True for boolean approach
    binary_vectorizer = CountVectorizer(tokenizer=nltk.word_tokenize, binary=True)
    binary_matrix = binary_vectorizer.fit_transform(documents)

    # Get feature names (terms)
    feature_names = binary_vectorizer.get_feature_names_out()

    # Convert binary matrix to a list for printing
    binary_matrix_list = binary_matrix.toarray().tolist()

    # Prepare a dictionary to store term presence in each document
    term_presence = {term: presence for term, presence in zip(feature_names, zip(*binary_matrix_list))}

    # Prepare the table data
    table_data = [[term] + [1 if presence else 0 for presence in term_presence[term]] for term in feature_names]

    # Print binary matrix in a table format with modified file names
    headers = ['Term'] + file_names  # Use modified file names without extension as headers

    print(tabulate(table_data, headers=headers))


if __name__ == '__main__':
    inverted_boolean()
