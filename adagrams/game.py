import random

def draw_letters():
    LETTER_POOL = {
    'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 
    'I': 9, 'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 
    'Q': 1, 'R': 6, 'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 
    'Y': 2, 'Z': 1
    }
    MAX_HAND_COUNT = 10
    all_available_let = []
    current_hand = []

    for letter, original_letter_count in LETTER_POOL.items():
        for letter_index in range(original_letter_count):
            all_available_let.append(letter)

    while len(current_hand) < MAX_HAND_COUNT:
        available_let_list_index = random.randint(0, len(all_available_let)-1)
        current_hand.append(all_available_let[available_let_list_index])
        all_available_let.pop(available_let_list_index)

    return current_hand

def uses_available_letters(word, letter_bank):
    word = word.upper()

    for input_letter in word:
        letter_freq_in_letter_bank = letter_bank.count(input_letter)
        letter_freq_in_word = word.count(input_letter)

        if input_letter not in letter_bank or letter_freq_in_word > letter_freq_in_letter_bank:
            return False
        
    return True

def score_word(word):

    points_dict = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 
    'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 
    'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 
    'Y': 4, 'Z': 10
    }
    word = word.upper()
    BONUS_POINTS = 8
    total_points = 0

    for input_letter in word:
        total_points += points_dict[input_letter]

    if len(word) >= 7:
        total_points += BONUS_POINTS

    return total_points

def get_highest_word_score(word_list):
    best_word = ''
    best_score = 0
    best_word_length = 0

    for word in word_list:
        word_score = score_word(word)
        word_length = len(word)

        if word_score > best_score:
            best_word = word
            best_score = word_score
            best_word_length = word_length
        elif word_score == best_score:
            if word_length == 10 and best_word_length != 10:
                best_word = word
                best_word_length = word_length
            elif word_length == 10 and best_word_length == 10:
                continue 
            elif word_length < best_word_length and best_word_length != 10:
                best_word = word
                best_word_length = word_length

    return best_word, best_score