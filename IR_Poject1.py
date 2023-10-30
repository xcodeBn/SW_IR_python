import os
import functools
import math
import re

from nltk.stem import PorterStemmer
from operator import itemgetter
import subprocess

from dependecy_installer import install_dependencies

install_dependencies()

with open("./stop_words_english.txt", "r", encoding="utf8") as readerst:
    datastop_words = readerst.read()
    stop_words = datastop_words.lower().replace("\n", " ").split(" ")
files_list = ['hello', 'how', 'amazing','no']


def filter(data):
    if isinstance(data, list):
        data = " ".join(data)
    list_of_words = data.lower().replace("\n", " ").split(" ")
    filter_list = {word for word in list_of_words if word not in stop_words and len(word) > 1}

    for word in filter_list:
        word = re.sub(r'[.|,:]$', '', word)

    return list(filter_list)


print(filter(stop_words))
