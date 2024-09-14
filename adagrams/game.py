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
    import random
    build an array (a hand) of 10 string
    a letter radomly draw from that pool
        2 avaialble C, return no more than 
        E can draw 12 times , Z considered 1 count
    user returns their hand to the pool before drawing new letters
    return 
    """
    draw_letters = []
    
    while len(draw_letters) < 10: #this loop will run until we have 10 letters in our hand
        
        random_letters = random.choices(list(letter_pool.keys()), list(letter_pool.values()))
        random_letter = random_letters[0]
        
        letter_count = draw_letters.count(random_letter) 
           
        if letter_count < letter_pool[random_letter]: 
            draw_letters.append(random_letter) 

                         
    return draw_letters
    
def uses_available_letters(word, letter_bank):
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
    create a dictionary to have key (letter) value(score) pair
    input: "str"
            if len(word) in rang(7,11) -> word += 8
    return int sum up of points of letters
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
    input : list of strings
    returns : tuple (a str, score)
    two words have the same score,
    pick the word with fewer letters.
    one of the tied words has exactly 10 letters, 
    pick that word.
    pick the word that appeared first in the list.
    """
    
    best_word = ""
    best_score = 0
    
    for word in word_list:
        score = score_word(word)
        # print(f"checking {word} , {score}")
        
        if score > best_score:
            best_word = word
            best_score = score
            # print(best_word, best_score)
        elif score == best_score:
            if len(word) < len(best_word) and len(best_word) != 10:
                best_word = word #update word with few letters but same score
            elif len(word) == 10 and len(best_word) != 10:
                best_word = word
    
    return best_word, best_score
       