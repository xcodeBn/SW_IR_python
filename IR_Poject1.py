import os
import functools
import math
from nltk.stem import PorterStemmer
from operator import itemgetter
import subprocess

# Define a function to install dependencies from a requirements file
def install_dependencies():
    requirements_file = "requirements.txt"

    if os.path.exists(requirements_file):
        subprocess.run(["pip", "install", "-r", requirements_file])
    else:
        print("Requirements file not found. Please create a 'requirements.txt' file.")


# Call the function to install dependencies
install_dependencies()

with open("./stop_words_english.txt", "r", encoding="utf8") as readerst:
    datastop_words = readerst.read()
    stop_words = datastop_words.lower().replace("\n", " ").split(" ")
files_list = []


def filter(data):
    list_of_words = data.lower().replace("\n", " ").split(" ")
    filter_list = [word for word in list_of_words if word not in stop_words and len(word) > 1]

    for elf in filter_list:
        if ".net" in elf:
            continue
        elif '@' in elf:
            if ".com" in elf or ".lb" in elf or ".gov" in elf or ".edu" in elf:
                continue
            else:
                filter_list.remove(elf)
        else:
            continue
    final_filter_list = []
    for dot in filter_list:
        if dot[-1] == "." or dot[-1] == "," or dot[-1] == ":":
            dotx = dot[:-1]
            dot = dotx
            final_filter_list.append(dot)
        elif "'" in dot:
            filter_list.remove(dot)
        else:
            final_filter_list.append(dot)
    filter_list = final_filter_list

    return filter_list

print(filter(stop_words))