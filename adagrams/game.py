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
score_chart_dict = {
    "1": ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
    "2": ['D', 'G'],
    "3": ['B', 'C', 'M', 'P'],
    "4": ['F', 'H', 'V', 'W', 'Y'],
    "5": ['K'],
    "8": ['J', 'X'],
    "10": ['Q', 'Z']
}

def draw_letters():
    letters_list = []
    random_draw_letters = []

    for letter, frequency in LETTER_POOL.items():
        for i in range(frequency):
            letters_list.append(letter)

    for i in range(10):
        random_index = random.randint(0, len(letters_list) - 1)
        random_draw_letters.append(letters_list[random_index])
        letters_list.pop(random_index)
    return random_draw_letters
    

def uses_available_letters(word, letter_bank):
    copy_letter_bank = list(letter_bank)
    word = word.upper()

    for letter in word:
        if letter in copy_letter_bank:
            copy_letter_bank.remove(letter)
        else:
            return False
    return True


def score_word(word):
    points_number = 0
    word = word.upper()

    for letter in word:
        for key, value in score_chart_dict.items():
            if letter in value:
                points_number += int(key)
    
    if len(word) >= 7:
        points_number += 8
    return points_number

def get_highest_word_score(word_list):
    best_word = word_list[0]
    best_score = score_word(word_list[0])

    for i in range(1, len(word_list)):
        word = word_list[i]
        word_score = score_word(word)

        if word_score > best_score:
            best_word = word
            best_score = word_score
        elif word_score == best_score:
            if len(word) == 10 and len(best_word) < 10:
                best_word = word
                best_score = word_score
            elif len(word) < len(best_word) and len(best_word) < 10:
                best_word = word
    return (best_word, best_score)
