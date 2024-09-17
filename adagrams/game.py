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
    ## pool_of_letters_array is an array that will store the letters and the number of times it occurs
    pool_of_letters_array = []

    ## for loop: iteration through LETTER_POOL to combine subset list into the pool_of_letters_array list
    for letter in LETTER_POOL: 
        pool_of_letters_array += list(letter * LETTER_POOL[letter])
    
    array_of_letters = pool_of_letters_array.copy()

    ## the use of while and if conditions ensures 10 random uniquely selected letters
    letter_list = []

    while len(letter_list) < 10:
        random_letter = random.choice(array_of_letters)
        letter_list.append(random_letter)
        array_of_letters.remove(random_letter)
        
    array_of_letters = pool_of_letters_array.copy()

    return letter_list


def uses_available_letters(word, letter_bank):
    word_alpha_list = []
    letter_bank_copy = letter_bank.copy()

    for letter in word:
        if letter in letter_bank_copy:
            popped_letter = letter_bank_copy.pop(letter_bank_copy.index(letter))
            word_alpha_list.append(popped_letter)
            
    if len(word_alpha_list) == len(word):
            return True

    elif letter not in letter_bank_copy and not letter.isupper():
        if len(word_alpha_list) < len(word):
            return word, letter_bank_copy

    else:
        return False

    return word, letter_bank


def score_word(word):
    BONUS_POINTS = 8
    points = 0

    for letter in word.upper():
        points += SCORE_CHART[letter]

    if len(word) >= 7 and len(word) <= 10:
        points += BONUS_POINTS

    return points


def get_highest_word_score(word_list):
    highest_word = word_list[0]
    highest_score = score_word(word_list[0])

    for word in word_list[1::]:
        current_score = score_word(word)
    
        if current_score > highest_score:
            highest_score = current_score
            highest_word = word
        elif current_score == highest_score:
            if len(highest_word) == 10:
                continue
            elif len(word) == 10:
                highest_word = word
            elif len(word) < len(highest_word):
                highest_word = word
    return highest_word, highest_score