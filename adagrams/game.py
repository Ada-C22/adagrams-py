import random

def draw_letters():
    list_letters = []
    distribution_of_letters = {
        "A":9,
        "B":2,
        "C":2,
        "D":4,
        "E":12,
        "F":2,
        "G":3,
        "H":2,
        "I":9,
        "J":1,
        "K":1,
        "L":4,
        "M":2,
        "N":6,
        "O":8,
        "P":2,
        "Q":1,
        "R":6,
        "S":4,
        "T":6,
        "U":4,
        "V":2,
        "W":2,
        "X":1,
        "Y":2,
        "Z":1
    }


    list_letters = []
    
    while len(list_letters) != 10:
        letters = list(distribution_of_letters.keys())
        random_letter = random.choice(letters)
        value = distribution_of_letters[random_letter]
        if value > 0:
            distribution_of_letters[random_letter] = value -1
            list_letters.append(random_letter)

    return list_letters

def uses_available_letters(word, letter_bank):
    word = word.upper()
    letters_copy = letter_bank[:]
    for letter in word:
        if letter in letters_copy:
            letters_copy.remove(letter)    
        else:
            return False
    return True

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass