import random
MAX_HAND_COUNT = 10

LETTER_POOL = {
    'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 
    'I': 9, 'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 
    'Q': 1, 'R': 6, 'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 
    'Y': 2, 'Z': 1
}

recorded_letters = {
    'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 
    'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 
    'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 
    'Y': 0, 'Z': 0
}

def draw_letters():
    best_keys_list_a = list(LETTER_POOL.keys())
    current_hand = []
    
    while len(current_hand) < 10:
    # for i in range(10):
        random_letter = random.choice(best_keys_list_a)
        current_hand.append(random_letter)
    
    return current_hand

# def draw_letters():
#     best_keys_list_a = list(LETTER_POOL.keys())
#     current_hand = []

#     while len(current_hand) < 10:
#         random_letter = random.choice(best_keys_list_a)
#         max_letter_quantity = LETTER_POOL[random_letter]

#         if recorded_letters[random_letter] < max_letter_quantity:
#             recorded_letters[random_letter] += 1
#             current_hand.append(random_letter)

#             # print(f'Pool: {random_letter, max_letter_quantity}')
#             print(f'Recorded: {random_letter, recorded_letters[random_letter], max_letter_quantity, recorded_letters[random_letter] <= max_letter_quantity}')
    
#     # print(recorded_letters)
#     print(f'Your hand {current_hand}')
#     print(f'Recorded: {recorded_letters[random_letter] <= max_letter_quantity}')

#     return current_hand

# def draw_letters():
#     best_keys_list_a = list(LETTER_POOL.keys())
#     current_hand = []

#     while len(current_hand) < 10:
#     # for i in range(10):
#         random_letter = random.choice(best_keys_list_a)
#         letter_pool_freq = LETTER_POOL[random_letter]
#         recorded_letters_freq = recorded_letters[random_letter]

#         if recorded_letters_freq < letter_pool_freq:
#             recorded_letters_freq += 1

#             current_hand.append(random_letter)
    
#     return current_hand





def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass