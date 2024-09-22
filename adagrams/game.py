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

SCORE_CHART = {
    1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
    2: ['D', 'G'],
    3: ['B', 'C', 'M', 'P'],
    4: ['F', 'H', 'V', 'W', 'Y'],
    5: ['K'],
    8: ['J', 'X'],
    10: ['Q', 'Z']
    }

def draw_letters():
    hand =[]
    copy_pool = {}

    index = 1
    for key, value in LETTER_POOL.items():
        copy_pool[index] = {key: value}
        index += 1
  
    while len(hand) < 10:
        letter_drawn = random.randint(1,26)
        letter_and_quantity = copy_pool[letter_drawn]
        for letter, quantity in letter_and_quantity.items():
            if quantity > 0:
                hand.append(letter)
                letter_and_quantity[letter] -= 1
    return hand


def deep_copy_letter_bank(letter_bank):
    letter_bank_copy = []
    for letter in letter_bank:
        letter_bank_copy += [letter]
    return letter_bank_copy


def uses_available_letters(word, letter_bank):
    
    copy_bank = deep_copy_letter_bank(letter_bank)
    word = word.upper()
    for letter in word:
        if letter in copy_bank:
            copy_bank.remove(letter)
        else:
            return False
    return True


def score_word(word):

    word = word.upper()
    total_score = 0
    
    if len(word) in range(7, 11):
        total_score += 8
    for letter in word:
        for score, letters in SCORE_CHART.items():
            if letter in letters:
                total_score += score
    return total_score


def get_highest_word_score(word_list):
   
    winning_word = None
    highest_score = 0

    for word in word_list:
        score = score_word(word)
        if score > highest_score:
            highest_score = score
            winning_word = word
        elif score == highest_score:
            if len(word) == 10 and len(winning_word) != 10:
                winning_word = word
            elif len(winning_word) != 10 and len(word) < len(winning_word):
                winning_word = word
    return winning_word, highest_score
