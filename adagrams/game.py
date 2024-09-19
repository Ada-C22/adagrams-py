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


def draw_letters():
# Create a list of letters using their frequencies
# pull letters from the list using random.randint
# create a new list from 10 random letters
    list_letters = []   

    for letter, freq in LETTER_POOL.items():
        for i in range (0,freq):
            list_letters.append(letter)

    #return list_letters

    hand = []
    b = len(list_letters)
    while len(hand)<10:
        index  = random.randint(0,b-1)
        new_letter = list_letters[index]
        if hand.count(new_letter) < LETTER_POOL[new_letter]:
            hand.append(new_letter)
    return hand

# Make all letter in word Capital
# function returns True or False

def uses_available_letters(word, letter_bank):

    #letter_bank = draw_letters()
    copy_letter_bank = letter_bank[:]
    word_up = word.upper()
    
    for letter in word_up:
        if letter not in copy_letter_bank or word_up.count(letter) > copy_letter_bank.count(letter):
            return False
    return True


# create a dictionary with points for each letter
# create new variable total_score, assign 0 to it
# for each letter add corresponding points from score dictionary
# if len(word) >= 7 add 8 points
# function returns score 

def score_word(word):
    total_score = 0
    word_up = word.upper()
    for letter in word_up:
        total_score += score_dict[letter]
    if len(word_up) >= 7 and len(word_up)<= 10:
        total_score += 8
    return total_score 
    
# create a dictionary with key as a word and value as a score
# iterate through the dictionary using items() method to get max_score
def get_highest_word_score(word_list):
    words_score_dict = {}
    for word in word_list:
        words_score_dict[word] = score_word(word)
    
# Look for max score, create variable max_score
# create a list of words with max score in case there are several words with same score
    max_score = 0
    max_score_words = []
    for word, w_score in words_score_dict.items():
        if w_score > max_score:
            max_score = w_score
            max_score_words = [word]
        elif w_score == max_score:
            max_score_words.append(word)
# print(max_score_words)        
# if there's one word with max score  

    if len(max_score_words) == 1:
        return (max_score_words[0], max_score) 
    
 # the case when there are several words with the same score   
    elif len(max_score_words) > 1:

        best_score_word = max_score_words[0]
    
        for word in max_score_words:
            if len(word) == 10:
                best_score_word = word
                return (best_score_word, max_score) 
           
            elif len(word)<len(best_score_word):
                best_score_word = word
                return (best_score_word, max_score) 
        return (best_score_word, max_score)    








