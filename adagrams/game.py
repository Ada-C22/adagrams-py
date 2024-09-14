
import random
from .data import LETTER_POOL
# wave 1 
# one letter per string and returns 10 
# letters are randomly distrubited while keeping count of the num 
# of letters. A has 9, B has 2 and so on.
# retun the str of 10 letters
# wave 1
def draw_letters():
    
    # store the letters
    hand =[]
    # to modify
    letter_counts = LETTER_POOL.copy()
    
    while len(hand)< 10:
        # create  a list of availbe letters
        avaiable_letters =[]
        for letter, count in letter_counts.items():
            if count > 0:
                avaiable_letters.append(letter)
        if not avaiable_letters:
            break
        # chose a random letter for avail letters
        choose_letter = random.choice(avaiable_letters)
    
        # add the chosen letter to our hand
        hand.append(choose_letter)
        # decrease the count of chose letter
        letter_counts[choose_letter] -=1
    # convert letter to str
    return ''.join(hand)
    

        
        
        
 # wave 2 
                        
def uses_available_letters(word, letter_bank):
    pass
    
def score_word(word):
    pass
    
def get_highest_word_score(word_list):
    pass