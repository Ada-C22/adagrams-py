import random

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

def draw_letters():
    letter_pool = LETTER_POOL.copy()
    letter_pool_keys = list(LETTER_POOL.keys())

    # have a variable with the list of chosen letters
    chosen_letters = []

    # use while loop to continue asking for random num 
    while len(chosen_letters) != 10:
        random_num = random.randint(0,25)
        random_letter = letter_pool_keys[random_num]

        if not letter_pool[random_letter]:
            continue

        chosen_letters.append(random_letter)
        letter_pool[random_letter] -= 1

    return chosen_letters

def uses_available_letters(word, letter_bank):
    if len(word) > len(letter_bank):
        return False
    
    word_uppercase = word.upper()

    available_letters_dict = {}
    for letter in letter_bank:
        if letter in available_letters_dict.keys():
            available_letters_dict[letter] += 1
        
        available_letters_dict[letter] = 1

    for letter in word_uppercase:
        if letter not in available_letters_dict.keys() or not available_letters_dict[letter] :
            return False
        
        available_letters_dict[letter] -= 1

    return True

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass