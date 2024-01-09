from inverted_boolean import inverted_boolean
from inverted_index import calculate_tfidf

if __name__ == '__main__':
    dir_name = "stemming_output"
    print("Project 3:")
    print("\nBOOLEAN_MODEL------------------------------------------------------------\n")
    inverted_boolean()
    print("\nTFIDF------------------------------------------------------------\n")
    calculate_tfidf(dir_name)


