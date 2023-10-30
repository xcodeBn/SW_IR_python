# Define a function to remove stop words from a list of words
import nltk


def remove_stop_words(words):
    """Removes stop words from a list of words.

    Args:
        words: A list of words.

    Returns:
        A list of words without stop words.
    """

    stopwords = nltk.corpus.stopwords.words('english')
    return [word for word in words if word not in stopwords]

# Define a function to remove stop words from a text file
def remove_stop_words_from_txt_file(input_file_path, output_file_path):
    """Removes stop words from a text file and writes the output to another text file.

    Args:
        input_file_path: The path to the input text file.
        output_file_path: The path to the output text file.
    """

    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        for line in input_file:
            words = line.split()
            filtered_words = remove_stop_words(words)
            output_file.write(' '.join(filtered_words) + '\n')

# Example usage:

# Remove stop words from a text file
input_file_path = 'input.txt'
output_file_path = 'output.stp'
remove_stop_words_from_txt_file(input_file_path, output_file_path)