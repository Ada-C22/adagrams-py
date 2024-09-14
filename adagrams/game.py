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

    weighted_list = []
    
    for letter, amount in LETTER_POOL.items():
	    weighted_list += letter * amount

    letters = []
    
    while len(letters) < 10:
        weighted_list_length = len(weighted_list)
        random_index = random.randrange(0,weighted_list_length)
        letters += weighted_list[random_index]
        weighted_list.pop(random_index)
        

    return letters
    
def uses_available_letters(word, letter_bank):
    word = word.upper()
    letters_in_word = ""

    for letter in letter_bank:
        if letter in word:
            letters_in_word += letter
    
    letters_in_word_list = list(letters_in_word)
    word_as_list = list(word)

    letters_in_word_list.sort()
    word_as_list.sort()

    if letters_in_word_list == word_as_list:
        return True
    else:
        return False


def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass