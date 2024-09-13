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

    final_string = []
    letters_frequency = []
    letters_list = []
    
    for letter_amount in LETTER_POOL:
        letters_frequency.append(LETTER_POOL[letter_amount])

    for letter in LETTER_POOL:
        letters_list.append(letter)

    while len(final_string) < 10:

        letter_index = random.randint(0, len(LETTER_POOL) -1)

        if letters_frequency[letter_index] > 0:
            letters_frequency[letter_index] -= 1
            final_string.append(letters_list[letter_index])
        
            
    return final_string

def uses_available_letters(word, letter_bank):
    available_letters = []


    for letter_item in letter_bank:
        available_letters.append(letter_item)

    for letter in word:
        uppercase_letter = letter.upper()
        if uppercase_letter in available_letters:
            
            available_letters.remove(uppercase_letter)
        else: 
            return False
    return True

def score_word(word):
    
    score = 0
    if len(word) > 7 and len(word) < 10:
        score += 8

def get_highest_word_score(word_list):
    pass