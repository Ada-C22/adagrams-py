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

def draw_letters():
    letter_list = [] 
    pool_letter_count = []

    for letter, count in LETTER_POOL.items():
        for _ in range(count):
            pool_letter_count.append(letter)
    
    while len(letter_list) < 10:
        letter_position = random.randint(0, len(pool_letter_count) -1)
        letter = pool_letter_count[letter_position]
        letter_list.append(letter)
        pool_letter_count.remove(letter)

    return letter_list 



def uses_available_letters(word, letter_bank):
    letter_bank_list = letter_bank.copy()
    word = word.upper()
    
    for letter in word:
        if letter in letter_bank_list:
            letter_bank_list.remove(letter)
        else:
            return False 
    return True 

    
def score_word(word):
    score_chart = {
        "A": 1, "E": 1, "I": 1, "O": 1, "U": 1, "L":1, "N": 1, "R": 1, "S":1, "T":1,
        "D": 2, "G": 2,
        "B": 3, "C": 3, "M": 3, "P": 3,
        "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4,
        "K":5 ,
        "J": 8, "X": 8, 
        "Q": 10, "Z": 10, 
    }
    score = 0 
    word = word.upper()
    
    for letter in word: 
        letter_point_value = score_chart[letter]
        score += letter_point_value 
    if len(word) >= 7: 
        score += 8 
    return score 


def get_highest_word_score(word_list):
    highest_score = 0
    highest_score_word = ""

    for word in word_list:
        current_score = score_word(word)
        if current_score > highest_score:
            highest_score = current_score
            highest_score_word = word 
        elif current_score == highest_score:
            if len(highest_score_word) == len(word) and len(highest_score_word) == 10:
                continue    
            elif len(word) < len(highest_score_word) and len(highest_score_word) < 10:
                highest_score_word = word
            elif len(highest_score_word) < 10 and len(word) == 10:
                highest_score_word = word 
                
    return highest_score_word, highest_score 



