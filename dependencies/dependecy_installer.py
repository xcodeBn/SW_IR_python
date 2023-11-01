import os
import subprocess
import pkg_resources
import nltk


def install_dependencies(requirements_file="requirements.txt"):
    # Check if the requirements file exists
    if os.path.exists(requirements_file):
        # Read the list of required packages from the requirements file
        with open(requirements_file, 'r') as file:
            required_packages = [line.strip() for line in file]

        # Check if each required package is already installed
        missing_packages = [package for package in required_packages if
                            not pkg_resources.get_distribution(package).parsed_version]

        if missing_packages:
            print(f"Installing missing dependencies: {missing_packages}")
            subprocess.run(["pip", "install", "-r", requirements_file])

        download_nltk_dependencies()

    else:
        print("Requirements file not found. Please create a 'requirements.txt' file.")


def download_nltk_dependencies():
    # Check if NLTK resources are present, and download them if not
    if not nltk.data.find("tokenizers/punkt"):
        print("Downloading NLTK Punkt tokenizer models...")
        nltk.download('punkt')

    if not nltk.data.find("corpora/stopwords"):
        print("Downloading NLTK stopwords corpus...")
        nltk.download('stopwords')

    if not nltk.data.find("corpora/wordnet"):
        print("Downloading NLTK WordNet corpus...")
        nltk.download('wordnet')



