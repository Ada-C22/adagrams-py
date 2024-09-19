
import random

def draw_letters():
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
    letters = ""
    for letter , num in letter_pool.items():
        letters += letter * num
    
    result = []
    letters_count_dict = {
    'A': 0, 
    'B': 0, 
    'C': 0, 
    'D': 0, 
    'E': 0, 
    'F': 0, 
    'G': 0, 
    'H': 0, 
    'I': 0, 
    'J': 0, 
    'K': 0, 
    'L': 0, 
    'M': 0, 
    'N': 0, 
    'O': 0, 
    'P': 0, 
    'Q': 0, 
    'R': 0, 
    'S': 0, 
    'T': 0, 
    'U': 0, 
    'V': 0, 
    'W': 0, 
    'X': 0, 
    'Y': 0, 
    'Z': 0
    }
    
    while len(result) < 10:
        i = random.randint(0, len(letters) - 1)
        if letter_pool[letters[i]] > letters_count_dict[letters[i]]:
            letters_count_dict[letters[i]] += 1
            result.append(letters[i])
    
    return result

def uses_available_letters(word, letter_bank):
    letter_bank_copy = []
    word_lower = word.lower()
    for letter in letter_bank:
        letter_bank_copy.append(letter.lower())

    for letter in word_lower:
        if letter not in letter_bank_copy:
            return False
        else:
            letter_bank_copy.remove(letter)
    return True

def score_word(word):
    score_dict = {
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
    sum_word = 0
    word_upper = word.upper()
    for letter in word_upper:
        sum_word += score_dict[letter]
    if len(word) >=7 and len(word) <= 10:
        sum_word += 8
    return sum_word


def get_highest_word_score(word_list):
    max_word = word_list[0]
    max_score = score_word(max_word)
    for i in range(1, len(word_list)):
        word = word_list[i]
        score = score_word(word)
        if score > max_score:
            max_score = score
            max_word = word 
        elif score == max_score and (len(word) != len(max_word)):
            if len(word) == 10:
                max_word = word
            elif len(word) < len(max_word) and len(max_word) != 10:
                max_word = word
    
    return (max_word, max_score)




