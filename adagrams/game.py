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
    letter_pool = []
    list = []
    hand_bank = []

    for letter_qunt in LETTER_POOL.items():
        list.append(letter_qunt)

    for letter_qunt in list:
        letter = letter_qunt[0]
        qunt = int(letter_qunt[1])
        while qunt > 0:
            letter_pool.append(letter)
            qunt = qunt - 1
    for idx in range(0, 10):
            idx = random.randint(0, len(letter_pool)-1)
            hand_bank.append(letter_pool[idx])
            del letter_pool[idx]
    return hand_bank
print(draw_letters())






def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass