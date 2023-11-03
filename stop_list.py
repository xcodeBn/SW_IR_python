import os
import re
import subprocess

from stemming import  perform_stemming
from util.dir_manager import get_directory

# Define the path to the stop words file
stop_words_path = "src/stop_words_english.txt"

# Create a set to store the stop words
stop_words = set()

# Read stop words from stop_words_english.txt
with open(stop_words_path, 'r', encoding="utf8") as stop_words_file:
    stop_words.update(word.strip() for word in stop_words_file)


# Function to remove stopwords from a list of words
def remove_stopwords(word_list, stopwords):
    # Define a regular expression to match only lowercase alphabetical characters
    regex = re.compile(r'[a-z]+')

    # Use list comprehension to filter words
    cleaned_words = [regex.findall(word.lower())[0] for word in word_list if regex.findall(word.lower())]

    # Check if cleaned words are not in stopwords
    return [word for word in cleaned_words if word not in stopwords]


# Function to manage stop words
def manage_stopwords():
    global stop_words
    # Ask the user if they want to edit the stop word list
    print("Current stop words:")
    for word in stop_words:
        print(word)

    user_choice = input("Do you want to edit the current stop word list? (yes/no): ").strip().lower()

    if user_choice == "yes":
        # Ask how many words the user wants to add (up to 10)
        num_words_to_enter = int(input("How many words would you like to add (max 10): "))
        num_words_to_enter = min(num_words_to_enter, 10)
        print("Enter the words to add:")
        new_words = set()
        for i in range(num_words_to_enter):
            word = input(f"Word {i + 1}: ").strip()
            new_words.add(word)
        stop_words.update(new_words)

        # Write the updated stopwords back to the stop_words_path file
        with open(stop_words_path, 'w', encoding="utf8") as stop_words_file:
            stop_words_file.write("\n".join(stop_words))


# Function to apply stopwords to a text
def apply_stopwords_to_text(text):
    words = text.split()
    filtered_words = remove_stopwords(words, stop_words)
    return " ".join(filtered_words)


# Function to process all ".txt" files in a directory and return the generated file names and paths
def process_directory(input_directory, output_directory):
    os.makedirs(output_directory, exist_ok=True)

    generated_files = []

    for filename in os.listdir(input_directory):
        if filename.endswith(".txt"):
            input_file_path = os.path.join(input_directory, filename)
            output_file_path = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}.stp")

            with open(input_file_path, 'r', encoding="utf8") as input_file:
                document_content = input_file.read()

            filtered_text = apply_stopwords_to_text(document_content)

            with open(output_file_path, 'w', encoding="utf8") as output_file:
                output_file.write(filtered_text)

            print(f"Stopwords removed from '{filename}' and saved to '{os.path.basename(output_file_path)}'.")
            generated_files.append(output_file_path)

    return generated_files


default_txt_file_directory = "example"
user_directory = get_directory(default_txt_file_directory)

if not user_directory:
    user_directory = "example"  # Default directory

# Define the output directory for processed files
output_directory = "output_files"

# Process the directory and get the list of generated files
generated_files = process_directory(user_directory, output_directory)

# Ask the user if they want to manage the stop words
manage_stopwords()

# Print the names and directories of the generated files
print("\nGenerated Files:")
for file_path in generated_files:
    print(file_path)

# Example usage with default directories:
perform_stemming()