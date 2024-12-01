import random
from collections import Counter

#creat letter pool 
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



def draw_letters():
    #make a copy of the letter pool
    user_pool = dict(LETTER_POOL)

    #create a list to sotre user drawn on hand
    hand = []
    
    letters = list(LETTER_POOL.keys())

    #use while loop to draw a random letter from letter pool
    while len(hand) < 10:
        # get all the letters from letter pool and store in a list
        

        # get a random index from the letters list
        random_index = random.randint(0, len(letters) -1)

        # get the random letter by using the random index
        random_letter = letters[random_index]
        # get the letter counts from the copy of letter pool, everytime draw a letter, the value update -1
        num = user_pool[random_letter]
        user_pool[random_letter] = num - 1

        #if no remaining letter in copy of letter pool, skip, and re-draw
        if user_pool[random_letter] <= 0:
            continue
        else:
            hand.append(random_letter)

    return hand
    
'''
    #use random.choice()
    # when the user has less 10 letter on hand, 
    # continue to drawn from the user pool, store in the list
    # if the remaining letter in user pool is 0,
    # jump to drawn a new letter.
    while len(hand) < 10:
        
        letter = random.choice(list(user_pool.keys()))
        
        num = user_pool[letter]

        user_pool[letter] = num - 1;
        
        if user_pool[letter] <= 0:
            continue
        else:
            hand.append(letter)
'''
    
    
    

def uses_available_letters(word, letter_bank):
    
    #initialize an empty dictinary to store the frequency of each letter
    frequency = {}

    #loop through each letter from the letter_bank,
    #if the letter in frequency{}, value +1
    #if not, add the letter to frequency{} and value 1
    for letter in letter_bank:
        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1  

    #check if word in letter_bank()
    #ignore the case sensitive
    #if the letter in the word,
    #and the freqency of the letter in word is lees than frequency of letter in letter bank, return True
    #else return False
    for letter in word.upper():
        if letter in frequency.keys():
            if frequency[letter] > 0:
                frequency[letter] -= 1
            else:
                return False
        else:
            return False
        
    return True

    '''
    #using Counter() method
    conuts = dict(Counter(letter_bank))
    print(conuts)

    #check if letter is in letter bank
    #
    for letter in word.upper():
        if letter in conuts.keys():
            if conuts[letter] > 0:
                conuts[letter] -= 1
            else:
                return False
        else:
            return False
    return True
    '''


SCORE_CHART = {
    ('A','E','I','O','U','L','N','R','S','T'):1,
    ('D','G'): 2,
    ('B','C','M','P'): 3,
    ('F','H','V','W','Y'): 4,
    ('K'):5,
    ('J','X'): 8,
    ('Q','Z'): 10
}


def score_word(word):
    
    #initiate a varaible to store the score
    score = 0

    #if the length of word is 7,8,9,10, the word gets an additional 8 points 
    if len(word) > 6:
        score += 8
    
    #get the score for each letter from the SCORE CHART, and sum
    for l in word.upper():
        for k, v in SCORE_CHART.items():
            if l in k:
                score += SCORE_CHART[k]
                continue 

    return score
        


def get_highest_word_score(word_list):
    #initiate an variable to store the best word
    best_word = ""

    #initiate an variable to store the hignest score
    highest_score = 0
    
    #look through the word in word list and find the highest score of the word
    for word in word_list:
        temp = score_word(word)
        temp_word = word
        if temp > highest_score:
            highest_score = temp
            best_word = temp_word
        #if tie:
        #prefer the word with the fewest letters...
        #unless one word has 10 letters. 
        #If the there are multiple words that are the same score and the same length, pick the first one in the supplied list
        elif temp == highest_score:
            if len(best_word) != 10 and (len(temp_word) == 10 or len(temp_word) < len(best_word)):
                highest_score = temp
                best_word = temp_word
                
    
    result = (best_word,highest_score)
    return result
