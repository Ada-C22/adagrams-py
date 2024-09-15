import random
import pytest

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
    # build a hand_letter_list
    letter_list = []
    # turning LETTER_POOL dictionary into a list
    for letter, count in LETTER_POOL.items():
        letter_list += [letter] * count
    # reture a hand of letters list
    return random.sample(letter_list, 10)


def uses_available_letters(word, letter_bank):
    word = word.upper()
    word_count = {}
    letter_bank_count = {}
    # count how many string in word
    for i in word:
        if i in word_count:
            word_count[i] += 1
        else:
            word_count[i] = 1

    # count how many string in letter_bank
    for y in letter_bank:
        if y in letter_bank_count:
            letter_bank_count[y] += 1
        else:
            letter_bank_count[y] = 1

    # compare word_count and letter_bank_count
    for key in word_count:
        if key in letter_bank_count:
            if word_count[key] != letter_bank_count[key]:
                return False
        else:
            return False
    
    return True


def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass