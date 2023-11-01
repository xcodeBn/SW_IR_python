import os
import nltk
from nltk.stem import WordNetLemmatizer


def perform_lemmatization(input_directory="output_files", output_directory="stemming_output"):
    # Initialize the WordNet lemmatizer
    lemmatizer = WordNetLemmatizer()

    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Remove old files in the output directory
    for old_file in os.listdir(output_directory):
        file_path = os.path.join(output_directory, old_file)
        if os.path.isfile(file_path):
            os.remove(file_path)

    # List all ".stp" files in the input directory
    stp_files = [f for f in os.listdir(input_directory) if f.endswith(".stp")]

    # Perform lemmatization on each ".stp" file
    for stp_file in stp_files:
        input_path = os.path.join(input_directory, stp_file)
        output_file = os.path.splitext(stp_file)[0] + ".sfx"
        output_path = os.path.join(output_directory, output_file)

        with open(input_path, 'r', encoding="utf8") as input_file:
            text = input_file.read()

        # Tokenize the text into words
        words = nltk.word_tokenize(text)

        # Apply lemmatization to each word based on its part of speech
        lemmatized_words = []
        for word in words:
            # Use WordNet part-of-speech tags
            pos_tag = nltk.pos_tag([word])[0][1][0].upper()
            pos_tag = pos_tag if pos_tag in ['A', 'N', 'R', 'V'] else 'N'  # Default to noun
            lemma = lemmatizer.lemmatize(word, pos_tag.lower())
            lemmatized_words.append(lemma)

        # Join the lemmatized words back into a string
        lemmatized_text = ' '.join(lemmatized_words)

        with open(output_path, 'w', encoding="utf8") as output_file:
            output_file.write(lemmatized_text)

    print(
        "Stemming and lemmatization completed. Lemmatized files are saved in the 'stemming_output' directory with the '.sfx' extension.")



