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

def draw_letters():
    hand_of_letters_list = []

    list_of_all_letters = []

    for letter,amount_of_that_letter in LETTER_POOL.items():
        for _ in range(amount_of_that_letter):
            list_of_all_letters.append(letter)

    while len(hand_of_letters_list) < 10:
        a_random_letter = random.randint(0, len(list_of_all_letters) - 1)
        random_letter_chosen = list_of_all_letters[a_random_letter]
        hand_of_letters_list.append(random_letter_chosen)
        list_of_all_letters.remove(random_letter_chosen)
         
    return hand_of_letters_list

draw_letters()

def uses_available_letters(word, hand_of_letters_list):
   
    '''
    Parameters:
        word (str): a word input by user
        hand_of_letters_list (list): an list of drawn letters (strings) in a hand.
    Returns:
        True: word bank is only using letters available in hand_of_letters_list
        False: word bank is using letters or other things not included in hand_of_letters_list
    '''
    
    word_bank_list = []

    for letter in hand_of_letters_list:
        word_bank_list.append(letter)

    for letter in word:
        letter = letter.upper()
        if letter not in word_bank_list:
            return False
        else:
            if letter in word_bank_list:
                word_bank_list.remove(letter)
    return True

def score_word(word):
    sum = 0

    for letter in word:
        letter = letter.upper()
        sum += LETTER_POINT_VALUES[letter]
    if len(word) >= 7:
        sum += 8
    return sum

def get_highest_word_score(word_list):
    winning_word_info = [] # ["word", score] index = [0, 1]

    for word in word_list:
        word_score = score_word(word)
        if not winning_word_info:
            winning_word_info = [word, word_score]
        elif word_score > winning_word_info[1]:
            winning_word_info = [word, word_score]
        elif word_score == winning_word_info[1]:
            if len(winning_word_info[0]) == 10:
                continue
            if len(word) == 10:
                winning_word_info = [word, word_score]
            elif len(word) < len(winning_word_info[0]):
                winning_word_info = [word, word_score]
                                                            
    winning_word_info_tuple = tuple(winning_word_info)

    return winning_word_info_tuple
