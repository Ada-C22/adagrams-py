
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
        available_letters =[]
        # check each letter and add ot availble_letters if greater than 0
        for letter, count in letter_counts.items():
            if count > 0:
                available_letters.append(letter)
        if not available_letters:
            break
        # chose a random letter for avail letters
        # my randon index generates a randon int between 0 and last index of availabe letters
        index = randint(0, len(available_letters) -1)
        choose_letter = available_letters[index]
        # decreases the count of the choosen letters 
        letter_counts[choose_letter] -= 1
        # this adds the choose letter to the hand list above 
        hand.append(choose_letter)
  
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

# wave 3
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

# wave 4
def get_highest_word_score(word_list):
    # initialize tuple, 1st stores the word, 2nd store the score
    highest_score = (None, 0)

    for word in word_list:
        # compare current_score with word
        new_score = score_word(word)
        # if new_scorre is greater then the highest_score
        if new_score > highest_score[1]:
            # update new high score in tuple
            highest_score = (word, new_score)
        # compair if  new_scores are tied if so move on
        elif new_score == highest_score[1]:
            # if len of the word equals 10 and the len of highet_score is not equal to 10
            if len(word) == 10 and len(highest_score[0]) != 10:
                highest_score = (word, new_score)
            # if no word is 10 letters long, and if the lenth of the word is shorter than high_score word chose the shorter word
            elif len(highest_score[0]) != 10 and len(word) < len(highest_score[0]):
                highest_score = (word, new_score)
                       
    return highest_score        
        
   
            



