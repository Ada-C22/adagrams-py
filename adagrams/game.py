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
    1 : ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
    2 : ["D", "G"],
    3 : ["B", "C", "M", "P"],
    4 : ["F", "H", "V", "W", "Y"],
    5 : ["K"],
    8 : ["J", "X"],
    10 : ["Q", "Z"]
}    

def draw_letters():
    letter_pool = []
    for letter, count in LETTER_POOL.items():
        for _ in range(count):
            letter_pool.append(letter)

    hand_of_letters = []
    while len(hand_of_letters) < 10:
        letter_index = random.randint(0, len(letter_pool)-1)
        hand_of_letters.append(letter_pool[letter_index])
        letter_pool.pop(letter_index)
    return hand_of_letters

draw_letters()

def uses_available_letters(word, letter_bank):

    capitalized_word = word.upper()
    letter_bank_copy = list(letter_bank)

    for letter in capitalized_word:
        if not letter in letter_bank_copy:
            return False
        else:
            letter_bank_copy.remove(letter)

    return True

def score_word(word):

    capitalized_word = word.upper()
    total_score = 0

    for letter in capitalized_word:
        for score, letters in SCORE_CHART.items():
            if letter in letters:
                total_score += score

    if 7 <= len(capitalized_word) <= 10:
        total_score += 8

    return total_score


def get_highest_word_score(word_list):

    highest_score = 0
    best_word = []

    for word in word_list :
        score = score_word(word)
        if score > highest_score:
            highest_score = score
            best_word = [word, score]
        elif score == highest_score:
            if len(word) == 10 and len(best_word[0])!= 10:
                best_word = [word, score]
            elif len(word) < len(best_word[0]) and len(best_word[0]) != 10:
                best_word = [word, score]
            elif len(word) == len(best_word[0]):
                continue
    
    return tuple(best_word)



