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


def draw_letters():
    """
    Draws a hand of 10 letters from a predefined pool.
    Returns:
        list of str: A list of 10 letters randomly drawn from the pool.
    Notes:
        letters are drawn according to their frequency in the pool.
        no letter will be drawn more times than its availability.
        the letter pool remains unchanged after drawing.
    """
    draw_letters = []
    letter_count = {}
    letters = []
       
    for letter, count in letter_pool.items():
        letters.extend([letter] * count)    
    # print(letters)
    
    while len(draw_letters) < 10:    
        letter_index = random.randint(0, len(letters)-1)
        random_letter = letters[letter_index]
        
        if random_letter not in draw_letters:
            #setting key and value to letter_count {}
            letter_count[random_letter] = 0
            
        #comparing the values of letter_count dict vs letter_pool dict
        if letter_count[random_letter] < letter_pool[random_letter]:
            draw_letters.append(random_letter)
            letter_count[random_letter] += 1
            
    return draw_letters         

def uses_available_letters(word, letter_bank):
    """
    Check if a word can be formed using the letters in letter bank
    Parameters:
        word(str)
        letter_bank(list of str)
    Return:
        Bool: True if every letter in available in letter bank
            False otherwise
    """
    letter_bank_copy = letter_bank[:]
    word = word.upper()
    
    for letter in word:
        if letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
        else:
            return False  
    return True

def score_word(word):
    """
    Create a dictionary to have key (letter) value(score) pair
    Parameters:
        word(str)
    Return:
        int: the total score of the word
    """
    total_score = 0
    word = word.upper()
    
    for letter in word:
        if letter in score_chart:
            total_score += score_chart[letter]
       
    if len(word) >= 7 and len(word) <= 10:
        total_score += 8
        
    return total_score

def get_highest_word_score(word_list):
    """
    Parameter:
        word_list(list of strings)
    returns : 
        tuple:
            highest score(str), the score(int)
    Notes:
        pick the word with fewer letters.
        one of the tied words has exactly 10 letters.
        pick the word that appeared first in the list.
    """
    
    best_word = ""
    best_score = 0
    
    for word in word_list:
        score = score_word(word)
        
        if score > best_score:
            best_word = word
            best_score = score
            
        elif score == best_score:
            if len(word) < len(best_word) and len(best_word) != 10:
                best_word = word 
            elif len(word) == 10 and len(best_word) != 10:
                best_word = word
    
    return best_word, best_score
       