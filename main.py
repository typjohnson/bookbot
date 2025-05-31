from stats import get_num_words, get_num_chars

def get_book_text(file_path):
    with open(file_path) as f:
        #the read method reads the contents of a file into a string
        file_contents = f.read()
        return file_contents

def main():
    text = get_book_text('books/frankenstein.txt')
    print(text)
    word_count = get_num_words(text)
    print(f"{word_count} words found in the document")
    print(get_num_chars(text))
   
    
main()