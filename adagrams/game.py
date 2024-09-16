import string
import random

def draw_letters():
    LETTER_POOL = {
        'A': 9, 
        'B': 2, 
        'C': 2, 
        'D': 4, 
        'E': 12, 
        'F': 2, 
        'G': 3, 
        'H': 2, 
        'I': 9, 
        'J': 1, 
        'K': 1, 
        'L': 4, 
        'M': 2, 
        'N': 6, 
        'O': 8, 
        'P': 2, 
        'Q': 1, 
        'R': 6, 
        'S': 4, 
        'T': 6, 
        'U': 4, 
        'V': 2, 
        'W': 2, 
        'X': 1, 
        'Y': 2, 
        'Z': 1
    }
    my_dictionary = {}
    my_list = []
    while len(my_dictionary) != 10:
        letter = random.choice(string.ascii_uppercase)
        if letter in my_dictionary:
            value = my_dictionary[letter]
            if value < LETTER_POOL[letter]:
                my_dictionary[letter] = value + 1
        else:
            my_dictionary[letter] = 1

    for key in my_dictionary:
        my_list.append(key)
    return my_list

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass