import random
import string
def draw_letters():
    hand_of_letters = []
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
    
    #iterate through the dict to convert letter_pool to a list
    LETTER_POOL_list = []  
    for letter,count in LETTER_POOL.items():
        while count > 0:
            LETTER_POOL_list.append(letter)
            count -=1    
   
    total_letter_count = len(LETTER_POOL_list)
    hand_of_letters = []
    #to get 10 letters 
    for i in range(10):
        #draw a random index from 0 to (totoal_letter_cout - i), given there are i letters
        #there are already drawn & put back as the last i items in the list
        draw_index = random.randrange(0, total_letter_count - i)
        hand_of_letters.append(LETTER_POOL_list[draw_index])
        # move the drawed letter to the end and won't be picked in next round
        #swith two items in the list : a, b = b,a
        LETTER_POOL_list[draw_index], LETTER_POOL_list[total_letter_count - i - 1] = \
            LETTER_POOL_list[total_letter_count - i - 1], LETTER_POOL_list[draw_index]

    return hand_of_letters


def uses_available_letters(word, letter_bank):
    """
    `word`, describes some input word, and is a string
    `letter_bank`, describes an array of drawn letters in a hand. 
    It is an array of ten strings, with each string representing an uppercase letter
    """
    letter_bank_count= {}
    for letter in letter_bank:
        if letter not in letter_bank_count:
            letter_bank_count[letter] = 1
        else:
            letter_bank_count[letter] += 1
    
    for char in word:
        if letter_bank_count.get(char,0) < 1:
            return False 
        letter_bank_count[char] -= 1
    
    return True


def score_word(word):
    score_chart = {
    'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
    'D': 2, 'G': 2,
    'B': 3, 'C': 3, 'M': 3, 'P': 3,
    'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
    'K': 5,
    'J': 8, 'X': 8,
    'Q': 10, 'Z': 10
    }
    score = 0
    word = word.upper()
    for char in word:
        score += score_chart[char]
    
    if 7 <= len(word) <= 10:
        score += 8
    return score 

def get_highest_word_score(word_list):
    
    max_score = 0
    max_word = None
    
    for word in word_list:
        score = score_word(word)
        if score > max_score:
            max_score = score
            max_word = word
        #how to break a tie
        #conditions that we need to update current max_word
        elif score == max_score and len(max_word)!= 10:
            if len(word) == 10 or len(word) < len(max_word):
                max_word = word

    return (max_word,max_score)


    


