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
LETTER_POINTS = {
    ("A", "E", "I", "O", "U", "L", "N", "R", "S", "T") : 1,
    ("D", "G"): 2,
    ("B", "C", "M", "P") : 3,
    ("F", "H", "V", "W", "Y") : 4,
    ("K") : 5,
    ("J", "X") : 8,
    ("Q", "Z") : 10
}

def draw_letters():
    letter_pool = LETTER_POOL.copy()
    letters = list(letter_pool.keys())

    chosen_letters = []
 
    while len(chosen_letters) < 10:
        random_index = random.randint(0,25)
        random_letter = letters[random_index]

        if not letter_pool[random_letter]:
            continue

        chosen_letters.append(random_letter)
        letter_pool[random_letter] -= 1

    return chosen_letters

def uses_available_letters(word, letter_bank):
    if len(word) > len(letter_bank):
        return False
    
    word_uppercase = word.upper()

    available_letters_dict = {}
    for letter in letter_bank:
        if letter in available_letters_dict.keys():
            available_letters_dict[letter] += 1
            continue
        
        available_letters_dict[letter] = 1

    for letter in word_uppercase:
        if letter not in available_letters_dict.keys() or not available_letters_dict[letter] :
            return False
        
        available_letters_dict[letter] -= 1

    return True

def score_word(word):
    score = 0

    word_uppercase = word.upper()
    for letter in word_uppercase:
        for letters, points in LETTER_POINTS.items():
            if letter in letters:
                score += points
    
    if len(word) in range(7,11):
        score += 8

    return score

def get_highest_word_score(word_list):
    highest_score = 0
    word_and_points_dict = {}
    
    for word in word_list:
        points = score_word(word)

        if points in word_and_points_dict.keys():
            word_and_points_dict[points].append(word)
        else:
            word_and_points_dict[points] = [word]

        if points > highest_score:
            highest_score = points


    # DETERMINE TIE BREAKER
    highest_scoring_words = word_and_points_dict[highest_score]

    if len(highest_scoring_words) < 2:
        return highest_scoring_words[0], highest_score
    
    shortest_word = highest_scoring_words[0]
    for word in highest_scoring_words:
        if len(word) == 10:
            return word, highest_score
        
        if len(word) < len(shortest_word):
            shortest_word = word
    
    return shortest_word, highest_score







