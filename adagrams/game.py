
LETTER_POOL = {
    1: {'A': 9},
    2: {'B': 2},
    3: {'C': 2},
    4: {'D': 4},
    5: {'E': 12},
    6: {'F': 2},
    7: {'G': 3},
    8: {'H': 2},
    9: {'I': 9},
    10: {'J': 1},
    11: {'K': 1},
    12: {'L': 4},
    13: {'M': 2},
    14: {'N': 6},
    15: {'O': 8},
    16: {'P': 2},
    17: {'Q': 1},
    18: {'R': 6},
    19: {'S': 4},
    20: {'T': 6},
    21: {'U': 4},
    22: {'V': 2},
    23: {'W': 2},
    24: {'X': 1},
    25: {'Y': 2},
    26: {'Z': 1}
}


def deep_copy_letter_pool(letter_pool):
    letter_pool_copy = {}
    for index, letters in letter_pool.items():
        letter_count = {}
        for letter, count in letters.items():
            letter_count[letter] = count
            letter_pool_copy[index] = letter_count
    return letter_pool_copy


def draw_letters():
    import random
    copy_pool = deep_copy_letter_pool(LETTER_POOL)
    hand = []
  
    while len(hand) < 10:
        letter_drawn = random.randint(1,26)
        letter_and_quantity = copy_pool[letter_drawn]
        for letter, quantity in letter_and_quantity.items():
            if quantity > 0:
                hand.append(letter)
                letter_and_quantity[letter] -= 1
    return hand


def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass