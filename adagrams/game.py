
import random
from .data import LETTER_POOL

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
        choose_letter = random.choice(avaiable_letters)
    
        # add the chosen letter to our hand
        hand.append(choose_letter)
        # decrease the count of chose letter
        letter_counts[choose_letter] -=1
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
    pass
    
def get_highest_word_score(word_list):
    pass


