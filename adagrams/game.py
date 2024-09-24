from string import ascii_uppercase
from random import randint

HAND_SIZE = 10
BONUS_LENGTH_MIN = 7
BONUS_POINTS = 8

def draw_letters():
    letter_pool = {
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

    # list_of_letters = []
    # for letter in LETTER_POOL:
    #     list_of_letters.extend(letter * LETTER_POOL[letter])
    # print(list_of_letters)

    hand = []

    while len(hand) < HAND_SIZE:
        random_letter = ascii_uppercase[randint(0, len(ascii_uppercase)-1)]
        if letter_pool[random_letter] > 0:
            hand.append(random_letter)
            letter_pool[random_letter] -= 1
    return hand


def uses_available_letters(word, letter_bank):
    letter_bank_list = list(letter_bank)

    for letter in word.upper():
        if letter in letter_bank_list:
            letter_bank_list.remove(letter)
        else:
            return False
    return True

draw_letters()

def score_word(word):
    SCORES_CHART = {
    'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
    'D': 2, 'G': 2,
    'B': 3, 'C': 3, 'M': 3, 'P': 3,
    'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
    'K': 5,
    'J': 8, 'X': 8,
    'Q': 10, 'Z': 10
}
    scores_total = 0
    for letter in word.upper():
        scores_total += SCORES_CHART[letter]
    if len(word) >= BONUS_LENGTH_MIN:
        scores_total += BONUS_POINTS
    return scores_total


def get_highest_word_score(word_list):
    highest_score = 0
    winner_word = ""

    for word in word_list:
        word_score = score_word(word)
        if word_score > highest_score:
            highest_score = word_score
            winner_word = word
        elif len(word) == HAND_SIZE and word_score == highest_score and len(winner_word) < HAND_SIZE:
            highest_score = word_score
            winner_word = word
        elif (word_score == highest_score
            and len(word) < len(winner_word)
            and len(winner_word) != HAND_SIZE):
            highest_score = word_score
            winner_word = word

    return (winner_word, highest_score)

