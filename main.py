from stats import get_num_words, get_num_chars, get_char_count_sorted

def get_book_text(file_path):
    with open(file_path) as f:
        #the read method reads the contents of a file into a string
        file_contents = f.read()
        return file_contents

def main():
    print("============ BOOKBOT ============")
    text = get_book_text('books/frankenstein.txt')
    print(f"Analyzing book found at {text}")
    print("----------- Word Count ----------")
    word_count = get_num_words(text)
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    char_count = get_num_chars(text)
    char_count_sorted = get_char_count_sorted(char_count)
    for key, value in char_count_sorted.items():
        if str(key).isalpha():
            print(f"{key}: {value}")
    print("============= END ===============")
   
    
    
main()