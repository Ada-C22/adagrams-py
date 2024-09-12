import random

def draw_letters():
    letter_map = {
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
    letter_pool = ['A','B','C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    result = []
    
    for i in range(10):
        letter = random.choice(letter_pool)
        result.append(letter)
        letter_map[letter] -= 1

        if letter_map[letter] == 0:
            letter_pool.remove(letter)
    
    return result

def uses_available_letters(word, letter_bank):
    upper_word = word.upper()
    copy_of_letter_bank = letter_bank[:]
    
    for letter in upper_word:
        if letter not in copy_of_letter_bank:
            return False
        
        copy_of_letter_bank.remove(letter)
    
    return True

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass

