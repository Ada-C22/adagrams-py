import random
MAX_HAND_COUNT = 10


LETTER_POOL = {
    'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 
    'I': 9, 'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 
    'Q': 1, 'R': 6, 'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 
    'Y': 2, 'Z': 1
}
points_dict = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 
    'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 
    'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 
    'Y': 4, 'Z': 10
    }

LETTERS_LIST = list(LETTER_POOL.keys())

def draw_letters():
    available_letters = LETTER_POOL.copy()
    current_hand = []

    while len(current_hand) < MAX_HAND_COUNT:
        random_letter = random.choice(LETTERS_LIST)

        if available_letters[random_letter] > 0:
            available_letters[random_letter] -= 1
            current_hand.append(random_letter)
        
        print(current_hand)

    return current_hand

def uses_available_letters(word, letter_bank):
    word = word.upper()

    for input_letter in word:
        letter_freq_in_letter_bank = letter_bank.count(input_letter)
        letter_freq_in_word = word.count(input_letter)
        # print(input_letter, letter_freq_in_letter_bank, letter_freq_in_word)

        if input_letter not in letter_bank or letter_freq_in_word > letter_freq_in_letter_bank:
            print(False)
            return False
        
    print(True)
    return True

def score_word(word):

    word = word.upper()
    BONUS_POINTS = 8
    total_points = 0

    for input_letter in word:
        total_points += points_dict[input_letter]

    if len(word) >= 7:
        total_points += BONUS_POINTS

    return total_points

def get_highest_word_score(word_list):
    word_score_board = {}
    best_score = 0
    best_word = ''

    for word in word_list:
        word_score_total = score_word(word)
        word_score_board[word] = word_score_total

    for word, word_score in word_score_board.items():
        if word_score > best_score:
            best_score = word_score
            best_word = word

        
    # print(best_score)
    print(best_word)
    return best_word, best_score
