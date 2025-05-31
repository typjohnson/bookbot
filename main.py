import sys
from stats import get_num_words, get_num_chars, get_char_count_sorted

#including the sys module to access command line arguments to give
#the CLI program greater capability for analyzing txt files.

#sys.argv returns a list of strings set as arguments for the program
if len(sys.argv) != 2:
    print('Please specify the program and a valid path...')
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)

def get_book_text(file_path):
    with open(file_path) as f:
        #the read method reads the contents of a file into a string
        file_contents = f.read()
        return file_contents

def main():
    print("============ BOOKBOT ============")
    text = get_book_text(sys.argv[1])
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