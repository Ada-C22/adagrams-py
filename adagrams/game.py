from string import ascii_uppercase
from random import randint



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
    hand = []

    while len(hand) < 10:
        pick = ascii_uppercase[randint(0, len(ascii_uppercase)-1)]
        if letter_pool[pick] > 0:
            hand.append(pick)
            letter_pool[pick] -= 1
    return hand


def uses_available_letters(word, letter_bank):
    word_list = list(word.upper())
    letter_bank_list = list(letter_bank)

    for letter in word_list:
        if letter in letter_bank_list:
            letter_bank_list.remove(letter)
        else:
            return False
    return True


def score_word(word):
    SCORES_CHART = {
    1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
    2: ['D', 'G'],
    3: ['B', 'C', 'M', 'P'],
    4: ['F', 'H', 'V', 'W', 'Y'],
    5: ['K'],
    8: ['J', 'X'],
    10: ['Q', 'Z']
}
    scores_total = 0
    for letter in word.upper():
        for score, letters_in_chart in SCORES_CHART.items():
            if letter in letters_in_chart:
                scores_total += score
    if len(word) >= 7:
        scores_total += 8
    return scores_total


def get_highest_word_score(word_list):
    highest_score = 0
    winner_word = ""

    for word in word_list:
        word_score = score_word(word)
        if word_score > highest_score:
            highest_score = word_score
            winner_word = word
        elif len(word) == 10 and word_score == highest_score and len(winner_word) < 10:
            highest_score = word_score
            winner_word = word
        elif (word_score == highest_score
            and len(word) < len(winner_word)
            and len(winner_word) != 10):
            highest_score = word_score
            winner_word = word

    return (winner_word, highest_score)

