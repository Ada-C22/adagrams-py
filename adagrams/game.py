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

LETTER_SCORES = {
    'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
    'D': 2, 'G': 2,
    'B': 3, 'C': 3, 'M': 3, 'P': 3,
    'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
    'K': 5,
    'J': 8, 'X': 8,
    'Q': 10, 'Z': 10
}

def draw_letters():
    letter_list = []
    for letter, letter_count in LETTER_POOL.items():
        for i in range(letter_count):
            letter_list.append(letter)
    hand = []
    for draw in range(10):
        hand_pick = random.randint(0, len(letter_list) -1)
        hand.append(letter_list[hand_pick])
        letter_list.pop(hand_pick)
    return hand 

def uses_available_letters(word, letter_bank):
    copy_letter_bank = list(letter_bank)
    upper_case_word = word.upper()

    for letter in upper_case_word:
        if letter in copy_letter_bank:
            copy_letter_bank.remove(letter)
        else:
            return False
    return True


def score_word(word):
    word = word.upper()
    total_score = 0

    for letter in word:
        total_score += LETTER_SCORES.get(letter, 0)
    
    if len(word) >= 7:
        total_score += 8
    
    return total_score

def get_highest_word_score(word_list):
    best_word = ""
    best_score = 0

    for word in word_list:
        current_score = score_word(word)

        if current_score > best_score:
            best_word = word
            best_score = current_score

        elif current_score == best_score:
            if len(word) == 10 and len(best_word) != 10:
                best_word = word
            elif len(word) < len(best_word) and len(best_word) != 10:
                best_word = word

    return (best_word, best_score)