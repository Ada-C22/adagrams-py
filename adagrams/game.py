import random

ORIGINAL_POOL = {
    "A" : 9,
    "B" : 2,
    "C" : 2,	
    "D" : 4,	  
    "E" : 12,	
    "F" : 2,	
    "G" : 3,	
    "H" : 2,	
    "I" : 9,	
    "J" : 1,	
    "K" : 1,	
    "L" : 4,	
    "M" : 2,
    "N" : 6,
    "O" : 8,
    "P" : 2,
    "Q" : 1,
    "R" : 6,
    "S" : 4,
    "T" : 6,
    "U" : 4,
    "V" : 2,
    "W" : 2,
    "X" : 1,
    "Y" : 2,
    "Z"	: 1
}


def draw_letters():

    copy_pool = {key: value for key, value in ORIGINAL_POOL.items()}
    pool = []
    
    while len(pool) < 10:
        index = random.randint(0, len(copy_pool.keys())-1)
        keys = copy_pool.keys()
        key = list(keys)[index] 
        if copy_pool[key] > 0:
            pool.append(key)
            copy_pool[key] = - 1          
    return pool

def uses_available_letters(word, letter_bank):
    word = word.upper()
    letter_bank = [letter.upper() for letter in letter_bank]

    for letter in word:
        if letter in letter_bank:
            letter_bank.remove(letter)
        else:
            return False
    return True


def score_word(word):
    score_chart = [
    {
        "letters" : ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
        "point": 1,
    },
    {
        "letters": ["D", "G"],
        "point":2,
    },
    {
        "letters": ["B", "C", "M", "P"],
        "point": 3,
    },
    {
        "letters": ["F", "H", "V", "W", "Y"],
        "point": 4,
    },
    {
        "letters":["K"],
        "point": 5,
    },
    {    
        "letters": ["J", "X"],
        "point": 8,
    },
    {
        "letters": ["Q", "Z"],
        "point": 10,
    }

    ]
    total = 0

    for letter in word.upper():
        for item in score_chart:
            if letter in item["letters"]:
                total += item["point"]

    if len(word) >= 7:
        total += 8

    return total

def get_highest_word_score(word_list):

    highest_score = 0
    selected_word = None

    for word in word_list:
        word_score = score_word(word)

        if word_score > highest_score:
            selected_word = word
            highest_score = word_score
        elif word_score == highest_score:
            if len(word) == 10 and len(selected_word) != 10:
                selected_word = word
            elif len(word) < len(selected_word) and len(selected_word) != 10:
                selected_word = word        

    return (selected_word, highest_score)



