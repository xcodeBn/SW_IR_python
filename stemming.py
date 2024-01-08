import os

from nltk.stem import SnowballStemmer

from util.habu_lib import remove_special_characters

# Set the Snowball Stemmer language
snowball_stemmer = SnowballStemmer("english")
P3-3
P3-3



def stem_text(text):
    words = text.split()

    stemmed_words = [snowball_stemmer.stem(remove_special_characters(word)) for word in words]
    return ' '.join(stemmed_words)


def perform_stemming(input_directory="output_files", output_directory="stemming_output"):
    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Remove old files in the output directory
    for old_file in os.listdir(output_directory):
        file_path = os.path.join(output_directory, old_file)
        if os.path.isfile(file_path):
            os.remove(file_path)

    # List all ".stp" files in the input directory
    stp_files = [f for f in os.listdir(input_directory) if f.endswith(".stp")]

    # Perform stemming on each ".stp" file
    for stp_file in stp_files:
        input_path = os.path.join(input_directory, stp_file)
        output_file = os.path.splitext(stp_file)[0] + ".sfx"
        output_path = os.path.join(output_directory, output_file)

        with open(input_path, 'r', encoding="utf8") as input_file:
            text = input_file.read()

        # Apply stemming to the text
        stemmed_text = stem_text(text)

        with open(output_path, 'w', encoding="utf8") as output_file:
            output_file.write(stemmed_text)
        # Print the name of the generated file
        print(f"Generated file: {output_file.name}")  # Extracting and printing the filename
    print("Stemming completed. Stemmed files are saved in the 'stemming_output' directory with the '.sfx' extension.")


