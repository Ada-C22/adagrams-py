import random

MAX_HAND_NUM = 10

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
    # random_index = random.randint(0, len(LETTER_POOL) - 1)
    random_letter = random.choice(LETTER_POOL.keys())

    for i in range(0,10):
        print(i)
        print(random_letter)

    return random_letter

draw_letters()

updated_letter_pool = {
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

current_hand = {
    'A': 0, 
    'B': 0, 
    'C': 0, 
    'D': 0, 
    'E': 0, 
    'F': 0, 
    'G': 0, 
    'H': 0, 
    'I': 0, 
    'J': 0, 
    'K': 0, 
    'L': 0, 
    'M': 0, 
    'N': 0, 
    'O': 0, 
    'P': 0, 
    'Q': 0, 
    'R': 0, 
    'S': 0, 
    'T': 0, 
    'U': 0, 
    'V': 0, 
    'W': 0, 
    'X': 0, 
    'Y': 0, 
    'Z': 0
}

used_hand = {
    'A': 0, 
    'B': 0, 
    'C': 0, 
    'D': 0, 
    'E': 0, 
    'F': 0, 
    'G': 0, 
    'H': 0, 
    'I': 0, 
    'J': 0, 
    'K': 0, 
    'L': 0, 
    'M': 0, 
    'N': 0, 
    'O': 0, 
    'P': 0, 
    'Q': 0, 
    'R': 0, 
    'S': 0, 
    'T': 0, 
    'U': 0, 
    'V': 0, 
    'W': 0, 
    'X': 0, 
    'Y': 0, 
    'Z': 0
}


