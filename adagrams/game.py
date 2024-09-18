
from random import randint
from .data import LETTER_POOL
from .score_chart import score_of_letters
# wave 1
def draw_letters():
    
    # store the letters
    hand =[]
    # makes copy of Letter_POOL so I can modifiy it and keep track of all letters used 
    letter_counts = LETTER_POOL.copy()
    
    while len(hand)< 10:
        # create  a list of availbe letters
        avaiable_letters =[]
        # check each letter and add ot availble_letters if greater than 0
        for letter, count in letter_counts.items():
            if count > 0:
                avaiable_letters.append(letter)
        if not avaiable_letters:
            break
        # chose a random letter for avail letters
        # my randon index generates a randon int between 0 and last index of availabe letters
        index = randint(0, len(avaiable_letters) -1)
        choose_letter = avaiable_letters[index]
        # decreases the count of the choosen letters 
        letter_counts[choose_letter] -= 1
        # this adds the choose letter to the hand list above 
        hand.append(choose_letter)
        # decrease the count of chose letter
        
    # convert letter to str
    return ''.join(hand)      
        
 # wave 2 
                        
def uses_available_letters(word, letter_bank):
    word = word.lower()
    
    for letter in word:
        # initialze letter found to false
        letter_found = False
        # loops to check each letter in the word
        for bank_letter in letter_bank:
            # if we find a match break out and goes to next statement
            if letter == bank_letter.lower():
                letter_found = True
                break
        # no need to continue if cannot form words
        if not letter_found:
            return False
        #  check if count of the letter in word is less or equal to the cound in letter bank
        # counts how many times the letter appears in the word
        word_count = word.count(letter)
        # initialze bank_count 
        bank_count = 0
        # loop through each bank_letter in the letter_bank 
        for bank_letter in letter_bank:
            # if bank_letter matches current letter + 1
            if letter == bank_letter.lower():
                bank_count += 1
        # this checks the word count to bank_count to how many time it appears in the bank if not enought letter will return False
        if word_count > bank_count:
            return False
    # refers back to the 1st for loop, and if there is enough letters to form a word then contiue on 
    return True
    
def score_word(word):
   # if the word has zero point the ret
    if not word:
        return 0
    
    # initialze variable to hold the total score
    total_score = 0
    # need to catch if user types lower case
    word = word.upper()
    
    # loop over the letters in the word
    for letter in word:
        # find the letter in the score_of_letters dict
        if letter.upper() in score_of_letters:
            # each letter value = looks at the score_of_letter in the dict and finds the number that is assocated to that letter
            letter_score =  score_of_letters[letter.upper()]
            # add to get total score
            total_score += letter_score
    # bonus, if there are 7 or more letters in the word then add 8 points to the total       
    if len(word) >= 7 :
        total_score += 8
            
    return total_score


# find highest score word
# from parm word_list is a list of str
# return tuple that represents the winning word
# tuple must have:
#   index 0 ([0]): a string of a word
#   index 1 ([1]): the score of the work
# for words that tie use tie break
#   word with fewest letter wins unless 10 letter
#   if top score is tied between multipul words and one is 10 letters long chose the 10 letter one over the other
# if all wors are the same score and lenth , pick the first one in the list
# 
def get_highest_word_score(word_list):
    pass


