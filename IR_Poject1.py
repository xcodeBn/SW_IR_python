import os

from dependencies.dependecy_installer import install_dependencies

install_dependencies()

import nltk
from nltk.corpus import stopwords

# Define the paths to the input src
stop_words_path = "src/stop_words_english.txt"
input_words_path = "example/example.txt"

# Create a set to store the stop words
stop_words = set()
nltk.download('stopwords')
print(stopwords.words('english'))

# Read stop words from stop_words_english.txt
with open(stop_words_path, 'r', encoding="utf8") as stop_words_file:
    stop_words.update(word.strip() for word in stop_words_file)

# Read words to remove from input.txt
with open(input_words_path, 'r', encoding="utf8") as input_words_file:
    words_to_remove = set(word.strip() for word in input_words_file)


def manage_stopwords():
    global words_to_remove
    # Ask the user if they want to edit the input.txt file
    user_choice = input("Do you want to edit the current stopword list? (yes/no): ").strip().lower()
    while (1 == 1):

        if user_choice == "yes":
            print("Current words in input.txt:")
            for word in words_to_remove:
                print(word)

            # Ask how many words the user wants to enter (up to 10)
            num_words_to_enter = int(input("How many words would you like to enter (max 10): "))
            num_words_to_enter = min(num_words_to_enter, 10)

            print("\nEnter the words:")
            new_words = set()
            for i in range(num_words_to_enter):
                word = input(f"Word {i + 1}: ").strip()
                new_words.add(word)

            words_to_remove.update(new_words)
        if(user_choice=="no"):
            break


manage_stopwords()

# Filter the stop words
filtered_stop_words = stop_words.difference(words_to_remove)

# Create the 'output_files' directory if it doesn't exist
output_directory = "output_files"
os.makedirs(output_directory, exist_ok=True)

# Save the filtered stop words to stop_words_english.stp
output_path = os.path.join(output_directory, "stop_words_english.stp")

with open(output_path, 'w', encoding="utf8") as output_file:
    output_file.write("\n".join(filtered_stop_words))

print("Filtered stop words saved to 'stop_words_english.stp' in 'output_files' directory.")
