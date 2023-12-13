from stemming import perform_stemming
from stop_list import handle_stopwords

if __name__ == '__main__':
    #remove the stop words
    handle_stopwords()
    # perform stemming after all is done
    perform_stemming()
    #do cosin stuff
    #enter query