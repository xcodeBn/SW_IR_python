import os

# Define the paths to the input files
stop_words_path = "stop_words_english.txt"
input_words_path = "files/input.txt"

# Create a set to store the stop words
stop_words = set()

# Read stop words from stop_words_english.txt
with open(stop_words_path, 'r', encoding="utf8") as stop_words_file:
    stop_words.update(word.strip() for word in stop_words_file)

# Read words to remove from input.txt
with open(input_words_path, 'r', encoding="utf8") as input_words_file:
    words_to_remove = set(word.strip() for word in input_words_file)

# Remove words to be excluded
filtered_stop_words = stop_words.difference(words_to_remove)

# Create the 'output_files' directory if it doesn't exist
output_directory = "output_files"
os.makedirs(output_directory, exist_ok=True)

# Save the filtered stop words to stop_words_english.stp
output_path = os.path.join(output_directory, "stop_words_english.stp")

with open(output_path, 'w', encoding="utf8") as output_file:
    output_file.write("\n".join(filtered_stop_words))

print("Filtered stop words saved to 'stop_words_english.stp' in 'output_files' directory.")
