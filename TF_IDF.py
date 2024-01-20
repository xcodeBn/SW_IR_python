import os
import math

import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

class TFIDFCalculator:
    def __init__(self, directory):
        self.directory = directory
        self.unique_words = self._gather_unique_words()
        self.term_frequency_matrix = self._calculate_tf_for_directory()
        self.idf_values = self._calculate_idf()

    def _gather_unique_words(self):
        files = [file for file in os.listdir(self.directory) if file.endswith('.sfx')]
        unique_words = set()

        for file in files:
            with open(os.path.join(self.directory, file), 'r', encoding='utf-8') as f:
                text = f.read()
                words = text.split()
                unique_words.update(words)

        unique_words = sorted(unique_words)
        return unique_words

    def _calculate_tf_for_directory(self):
        files = [file for file in os.listdir(self.directory) if file.endswith('.sfx')]
        term_frequency_matrix = pd.DataFrame(columns=self.unique_words)
        term_frequency_matrix['File'] = files
        term_frequency_matrix = term_frequency_matrix.set_index('File')

        for file in files:
            with open(os.path.join(self.directory, file), 'r', encoding='utf-8') as f:
                text = f.read()

                for word in self.unique_words:
                    tf = text.split().count(word)
                    term_frequency_matrix.loc[file, word] = tf

        return term_frequency_matrix

    def _calculate_idf(self):
        total_documents = len(self.term_frequency_matrix)
        idf_values = {}

        for word in self.unique_words:
            doc_count = sum(self.term_frequency_matrix[word] > 0)
            idf = math.log10(total_documents / doc_count)
            idf_values[word] = idf

        return idf_values

    def calculate_tfidf(self):
        tfidf_matrix = self.term_frequency_matrix.copy()
        for word in tfidf_matrix.columns:
            tfidf_matrix[word] = tfidf_matrix[word] * self.idf_values[word]

        return tfidf_matrix

    def calculate_cosine_similarity_v1(self,A, B):
        # Calculate dot product
        dot_product = sum(a * b for a, b in zip(A, B))

        # Calculate the magnitude of each vector
        magnitude_A = sum(a * a for a in A) ** 0.5
        magnitude_B = sum(b * b for b in B) ** 0.5

        # Compute cosine similarity
        cosine_similarity = dot_product / (magnitude_A * magnitude_B)

        return cosine_similarity
    def cosine_similarity(self,matrix1, matrix2):
        dot_product = np.dot(matrix1, matrix2)  # Transpose matrix2 to make dimensions compatible
        norm1 = np.linalg.norm(matrix1)
        norm2 = np.linalg.norm(matrix2)

        similarity = dot_product / (norm1 * norm2)

        return similarity
    def calculate_cosine_similarity(self, query, should_round = False):
        # Calculate TF-IDF for the query
        query_tfidf = pd.DataFrame(columns=self.unique_words)
        query_tfidf.loc[0] = 0  # Initialize the row for the query
        for word in self.unique_words:
            tf = query.split().count(word)
            query_tfidf.loc[0, word] = tf * self.idf_values[word]

        print("Query TF-IDF:")
        print(query_tfidf)

        # Calculate cosine similarity between the query and documents
        similarity_matrix = cosine_similarity(self.calculate_tfidf(), query_tfidf)

        # Extract the similarity scores for the query
        query_similarity_scores = similarity_matrix[:, 0]

        # Create a DataFrame to display results
        similarity_results_ = pd.DataFrame({
            'File': self.term_frequency_matrix.index,
            'Similarity': query_similarity_scores
        })

        # Sort by similarity in descending order
        similarity_results_ = similarity_results_.sort_values(by='Similarity', ascending=False)



        return similarity_results_

    def save_inverted_file(self):
        return 0






if __name__ == '__main__':
    tfidf_calculator = TFIDFCalculator(directory="stemming_output")

    # Get user query

    tfidf_matrix = tfidf_calculator.calculate_tfidf()
    print("\nTF IDF MATRIX")
    print(tfidf_matrix)
    # Calculate cosine similarity
    user_query = input("Enter your query: ")

    similarity_results = tfidf_calculator.calculate_cosine_similarity(user_query)

    # Display the results
    print("\nCosin Similarity Results:")
    print(similarity_results)
