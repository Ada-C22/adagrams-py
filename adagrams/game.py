import random

HAND_SIZE = 10

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

LETTER_POINT_VALUES = {
    'A': 1, 
    'B': 3, 
    'C': 3, 
    'D': 2, 
    'E': 1, 
    'F': 4, 
    'G': 2, 
    'H': 4, 
    'I': 1, 
    'J': 8, 
    'K': 5, 
    'L': 1, 
    'M': 3, 
    'N': 1, 
    'O': 1, 
    'P': 3, 
    'Q': 10, 
    'R': 1, 
    'S': 1, 
    'T': 1, 
    'U': 1, 
    'V': 4, 
    'W': 4, 
    'X': 8, 
    'Y': 4, 
    'Z': 10
}

def create_letter_pool():
    list_of_all_letters = []
    list_of_all_letters = [letter for letter, letter_frequency in LETTER_POOL.items() for _ in range(letter_frequency)]

    return list_of_all_letters

def draw_letters():
    hand_of_letters_list = []
    list_of_all_letters = create_letter_pool()
 
    while len(hand_of_letters_list) < HAND_SIZE:
        a_random_index_that_accesses_random_letter = random.randint(0, len(list_of_all_letters) - 1)
        random_letter_chosen = list_of_all_letters[a_random_index_that_accesses_random_letter]
        hand_of_letters_list.append(random_letter_chosen)
        list_of_all_letters.remove(random_letter_chosen)
         
    return hand_of_letters_list

def uses_available_letters(word, hand_of_letters_list):
   
    '''
    Parameters:
        word (str): a word input by user
        hand_of_letters_list (list): an list of drawn letters (strings) in a hand.
    Returns:
        True: word_bank_list is only using letters available in hand_of_letters_list
        False: word_bank_list is using letters or other things not included in hand_of_letters_list
    '''

    word_bank_list = []
    word_bank_list = [letter for letter in hand_of_letters_list]

    for letter in word.upper():
        if letter not in word_bank_list:
            return False
        else:
            if letter in word_bank_list:
                word_bank_list.remove(letter)
    return True

def score_word(word):
    total_score = 0

    for letter in word.upper():
        total_score += LETTER_POINT_VALUES[letter]
    if len(word) >= 7:
        total_score += 8
    return total_score

def get_highest_word_score(word_list):
    winning_word = None 
    winning_score = 0

    for word in word_list:
        word_score = score_word(word)

        if winning_word is None:
            winning_word = word
            winning_score = word_score
        elif word_score > winning_score:
            winning_word = word
            winning_score = word_score
        elif word_score == winning_score:
            if len(winning_word) == 10:
                continue
            if len(word) == 10:
                winning_word = word
                winning_score = word_score
            elif len(word) < len(winning_word):
                winning_word = word
                winning_score = word_score

    return winning_word, winning_score