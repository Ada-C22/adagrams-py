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
    word_dictionary = {}
    for letter in word.upper():
        if letter in word_dictionary:
            value = word_dictionary[letter]
            word_dictionary[letter] = value + 1
        else:
            word_dictionary[letter] = 1

    for letter in letter_bank:
        if letter in word_dictionary:
            value = word_dictionary[letter]
            word_dictionary[letter] = value - 1
    return sum(word_dictionary.values()) == 0

def score_word(word):
    LETTER_SCORES = {
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
    total_points = 0
    for letter in word.upper():
        if letter in LETTER_SCORES:
            value = LETTER_SCORES[letter]
            total_points += value
    if len(word) == 7 or len(word) == 8 or len(word) == 9 or len(word) == 10:
        total_points = total_points + 8
    return total_points

def get_highest_word_score(word_list):
    LETTER_SCORES = {
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
    
    word_result = ['0',0]
    for current_word in word_list:
        current_sum = 0
        for letter in current_word:
            key = letter.upper()
            current_sum = current_sum + LETTER_SCORES[key]

        if len(current_word) == 10:
            current_sum = current_sum + 8

        previous_sum = word_result[1] 
        previous_word = word_result[0]

        if previous_sum < current_sum:
            word_result[0] = current_word
            word_result[1] = current_sum  
        elif previous_sum == current_sum:
            previous_size = len(previous_word)
            current_size = len(current_word)

            if(current_size==10 and previous_size !=10):
                word_result[0] = current_word
            elif current_size!=10 and previous_size !=10 and current_size < previous_size:
                word_result[0] = current_word
                
    return tuple(word_result)
