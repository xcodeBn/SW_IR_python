import os
import math
import pandas as pd


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


if __name__ == '__main__':
    tfidf_calculator = TFIDFCalculator(directory="stemming_output")
    tfidf_matrix = tfidf_calculator.calculate_tfidf()
    print(tfidf_matrix)
