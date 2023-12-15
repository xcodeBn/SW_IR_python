from inverted_boolean import inverted_boolean
from tfidf_test import calculate_tfidf

if __name__ == '__main__':
    dir_name = "stemming_output"
    print("Project 3:")
    print("------------------------------------------------------------\n")
    inverted_boolean()
    print("------------------------------------------------------------\n")
    calculate_tfidf(dir_name)


