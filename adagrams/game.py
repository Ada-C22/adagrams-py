import random

LETTER_POOL = ["A","A","A","A","A","A","A","A","A","B","B","C","C","D","D","D","D","E","E","E","E","E","E","E","E","E","E","E","E","F","F","G","G","G","H","H","I","I","I","I","I","I","I","I","I","J","K","L","L","L","L","M","M","N","N","N","N","N","N","O","O","O","O","O","O","O","O","P","P","Q","R","R","R","R","R","R","S","S","S","S","T","T","T","T","T","T","U","U","U","U","V","V","W","W","X","Y","Y","Z"]

LETTER_POINTS = {
    "A" : 1,
    "E" : 1,
    "I" : 1,
    "O" : 1,
    "U" : 1,
    "L" : 1,
    "N" : 1,
    "R" : 1,
    "S" : 1,
    "T" : 1,
    "D" : 2,
    "G" : 2,
    "B" : 3,
    "C" : 3,
    "M" : 3,
    "P" : 3,
    "F" : 4,
    "H" : 4,
    "V" : 4,
    "W" : 4,
    "Y" : 4,
    "K" : 5,
    "J" : 8,
    "X" : 8,
    "Q" : 10,
    "Z" : 10
}

def draw_letters():
    letter_pool = LETTER_POOL.copy()
    chosen_letters = []
 
    while len(chosen_letters) < 10:
        random_index = random.randint(0,len(letter_pool)-1)
        random_letter = letter_pool.pop(random_index)
        chosen_letters.append(random_letter)

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

    for letter in word.upper():
        if letter in LETTER_POINTS:
            score += LETTER_POINTS[letter]
    
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







