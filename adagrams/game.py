import random

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

def draw_letters():
    """
    import random 
    build an array (a hand) of 10 string
    a letter randomly draw from that pool
    """ 

    # generates a position for letter
    
    # convert letter pool into lists
    letter_list, usage_list = list(letter_pool.keys()), list(letter_pool.values())
    
    # generate a random letter
    hand = []
    
    while len(hand) < 10:
        position = random.randint(0, len(letter_list)-1)
        letter_frequency = usage_list[position]
        random_letter = letter_list[position]
        
        if hand.count(random_letter) < letter_frequency:
            add_letter = hand.append(random_letter)
            # print(f"{hand.count(random_letter)}, {random_letter}")
        else:
            continue
    return hand

draw_letters()


def uses_available_letters(word, letter_bank):
    pass
            


def score_word(word):
    pass


def get_highest_word_score(word_list):
    pass