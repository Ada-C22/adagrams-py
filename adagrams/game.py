import random

def draw_letters():
    
    letter_pool_str= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # List comp for converting ABC string on line 7 into list 
    letter_pool_list = [letter for letter in letter_pool_str]
    
    # Original letter pool dict - stays constant
    letter_pool_dict = {
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
    # Tracking container: where the letters(key) and their freq (value) will be stored as separate dictionaries
    tracking_letter_dict = {
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

    # List of randomly drawn hand, stores 10 letters or tiles
    hand = []
    
    # Adding a random letter to the hand, and reducing frequency for each draw
    while len(hand) < 10:
        random_letter = letter_pool_list[random.randint(0, 25)]
        initial_letter_count = letter_pool_dict[random_letter]
        random_letter_count = tracking_letter_dict[random_letter]
        if 0 < random_letter_count <= initial_letter_count:
            hand.append(random_letter)
            tracking_letter_dict[random_letter] -= 1 # *** Located and fixed bug causing one-off error ***
            
    return hand

def uses_available_letters(word, letter_bank):
    # Copies of arguments to stay in the "safe" zone:
    letter_bank_copy = [letter for letter in letter_bank]
    uppercase_word = word.upper()
    word_list_copy = [letter for letter in uppercase_word]

    # Flag bool variable - default set to True
    letter_check = True

    for letter in word_list_copy:
        # Checks if a letter in word is not in the letter bank
        if letter not in letter_bank_copy:

            # Flag set to False - will return False for entire function
            letter_check = False

        # If letter in word is found in letter bank
        # remove the letter, to signal it has been used
        elif letter in letter_bank_copy:
            letter_bank_copy.remove(letter)

    
    return letter_check
    
    
def score_word(word):
    # Score Dictionary:
    score_dict = {
        "A": 1,
        "E": 1,
        "I": 1,
        "O": 1,
        "U": 1,
        "L": 1,
        "N": 1,
        "R": 1,
        "S": 1,
        "T": 1,
        "D": 2,
        "G": 2,
        "B": 3,
        "C": 3,
        "M": 3,
        "P": 3,
        "F": 4,
        "H": 4,
        "V": 4,
        "W": 4,
        "Y": 4,
        "K": 5,
        "J": 8,
        "X": 8,
        "Q": 10,
        "Z": 10
    }
    
    uppercase_word = word.upper()
    score_count = 0
    
    if 7 <= len(uppercase_word) <= 10:
        score_count += 8
        
    for letter in list(uppercase_word):
        if letter in score_dict:
            score_count += score_dict[letter]
    return score_count


########     WAVE 4   ################
######## Helper Functions ###########
# Get/generate list of tupes for all words in word_list where tuple = ("word", word_score)
def get_score_list(word_list):

    word_scores = []
    for i in range(len(word_list)):

        #Calculate score of current word
        current_word = word_list[i]
        current_word_score = score_word(current_word)

        # Add tuple of (current word, current word score) to 
        word_scores.append((current_word, current_word_score))

    return word_scores # returns list of tuples ("word", word score)


def get_max_score(word_list):
    #Constants
    WORD_INDEX = 0
    SCORE_INDEX = 1
    
    # Call list of tuples from helper function: get_score_list(word_list)
    all_word_scores = get_score_list(word_list) 

    # Assume the first item's word score in list of tuples is the max-score
    # Change current_max_score if loop comes across a larger value
    current_max_score = all_word_scores[WORD_INDEX][SCORE_INDEX]

    for word, score in all_word_scores:
        # Iterate and check which score is the highest: 
        if score > current_max_score:
            current_max_score = score
            
        else:
            continue
    return current_max_score


def get_shortest_len(final_list):

    WORD_IDX = 0
    shortest_len = len(final_list[0][WORD_IDX])

    for i in range(len(final_list)):
        if len(final_list[i][WORD_IDX]) < shortest_len:
            shortest_len = len(final_list[i][WORD_IDX])

    # integer of shortest length of string in final_list
    return shortest_len 


# WAVE 4 FUNCTION - to be tested #
def get_highest_word_score(word_list):

    highest_score = get_max_score(word_list)
    all_word_scores = get_score_list(word_list)
    high_score_words = []

    for current_word, current_score in all_word_scores:

        if current_score == highest_score:
            high_score_words.append((current_word, current_score))

        else:
            continue
    
    
    shortest_len = get_shortest_len(high_score_words)
    high_score_pair = () # return value for function with (word, score)

    for final_word, final_score in high_score_words:
        if len(high_score_words) == 1:
            high_score_pair = high_score_pair = (final_word, final_score)
            return high_score_pair
        
        elif len(final_word) < 10 and len(final_word) == shortest_len: 
            high_score_pair = (final_word, final_score)
        
        elif len(final_word) == 10:
            high_score_pair = (final_word, final_score)
            return high_score_pair

    return high_score_pair
        
        

        





        

        


    












        


        








