
def get_num_words(text):
    word_count = len(text.split())
    return word_count

#function to get the number of ALL characters
#disregarding case and including symbols/spaces
def get_num_chars(text):
    char_count = {}
    for char in text.lower():
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count