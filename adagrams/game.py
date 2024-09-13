import random

def draw_letters():
    letter_map = {
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
    letter_pool = ['A','B','C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    result = []
    
    for i in range(10):
        letter = random.choice(letter_pool)
        result.append(letter)
        letter_map[letter] -= 1

        if letter_map[letter] == 0:
            letter_pool.remove(letter)
    
    return result

def uses_available_letters(word, letter_bank):
    upper_word = word.upper()
    copy_of_letter_bank = letter_bank[:]
    
    for letter in upper_word:
        if letter not in copy_of_letter_bank:
            return False
        
        copy_of_letter_bank.remove(letter)
    
    return True

def score_word(word):
    score_chart = {
    'A': 1, 
    'B': 3, 
    'C': 3, 
    'D': 2, 
    'E': 1, 
    'F': 4, 
    'G': 2, 
    'H': 4, 
    'I': 1, 
    'J': 8, 
    'K': 5, 
    'L': 1, 
    'M': 3, 
    'N': 1, 
    'O': 1, 
    'P': 3, 
    'Q': 10, 
    'R': 1, 
    'S': 1, 
    'T': 1, 
    'U': 1, 
    'V': 4, 
    'W': 4, 
    'X': 8, 
    'Y': 4, 
    'Z': 10
}
    score = 0
    upper_word = word.upper()

    for letter in upper_word:
        score += score_chart[letter]

    if len(word) >= 7:
        score += 8

    return score

def get_highest_word_score(word_list):
    highest_score = 0
    
    for word in word_list:
        score = score_word(word)
        if score < highest_score:
            continue
        elif score == highest_score and len_of_highest_score_word == 10:
            continue
        elif score == highest_score and len(word) != 10 and len(word)> len_of_highest_score_word:
            continue

        highest_score = score
        highest_score_word = word
        len_of_highest_score_word = len(word)
       
    return (highest_score_word, highest_score)
    