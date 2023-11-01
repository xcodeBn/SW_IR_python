import os

# Define the paths to the input files
stop_words_path = "src/stop_words_english.txt"
document_file = "example/example.txt"

# Create a set to store the stop words
stop_words = set()

# Read stop words from stop_words_english.txt
with open(stop_words_path, 'r', encoding="utf8") as stop_words_file:
    stop_words.update(word.strip() for word in stop_words_file)

# Read the content from the document file and tokenize it into words
with open(document_file, 'r', encoding="utf8") as input_words_file:
    document_content = input_words_file.read()
    words = document_content.split()


# Function to remove stopwords from the list of words
def remove_stopwords(word_list, stopwords):
    return [word for word in word_list if word.lower() not in stopwords]


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


# Remove stopwords from the words
filtered_words = remove_stopwords(words, stop_words)

# Create an output directory
output_directory = "output_files"
os.makedirs(output_directory, exist_ok=True)

# Save the cleaned text to a new file with the ".stp" extension
output_filename = os.path.splitext(os.path.basename(document_file))[0] + ".stp"
output_path = os.path.join(output_directory, output_filename)

with open(output_path, 'w', encoding="utf8") as output_file:
    output_file.write(" ".join(filtered_words))

# Ask the user if they want to manage the stop words
manage_stopwords()

print(f"Stopwords removed and saved to '{output_filename}' in 'output_files' directory.")
