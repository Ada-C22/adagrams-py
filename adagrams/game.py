
from random import randint
from .data import LETTER_POOL
from .score_chart import score_of_letters
# wave 1
def draw_letters():
    
    hand =[]
    letter_counts = LETTER_POOL.copy()
    
    while len(hand)< 10:

        available_letters =[]
       
        for letter, count in letter_counts.items():
            if count > 0:
                available_letters.append(letter)
        if not available_letters:
            break
        
        index = randint(0, len(available_letters) -1)
        choose_letter = available_letters[index]
        letter_counts[choose_letter] -= 1
        hand.append(choose_letter)
  
    return hand   

 # wave 2 
                        
def uses_available_letters(word, letter_bank):
    word = word.lower()
    
    for letter in word:
       
        letter_found = False
        
        for bank_letter in letter_bank:
            if letter == bank_letter.lower():
                letter_found = True
                break
        if not letter_found:
            return False
        word_count = word.count(letter)
       
        bank_count = 0
       
        for bank_letter in letter_bank:
    
            if letter == bank_letter.lower():
                bank_count += 1
        if word_count > bank_count:
            return False
    return True

# wave 3
def score_word(word):
  
    if not word:
        return 0
    
    total_score = 0
    
    word = word.upper()
    
    for letter in word:
       
        if letter.upper() in score_of_letters:
            letter_score =  score_of_letters[letter.upper()]
            total_score += letter_score      
    if len(word) >= 7 :
        total_score += 8
            
    return total_score  

# wave 4
def get_highest_word_score(word_list):
    
    highest_score = (None, 0)

    for word in word_list:
        new_score = score_word(word)
        if new_score > highest_score[1]:
            highest_score = (word, new_score)
        elif new_score == highest_score[1]:
            if len(word) == 10 and len(highest_score[0]) != 10:
                highest_score = (word, new_score)
            elif len(highest_score[0]) != 10 and len(word) < len(highest_score[0]):
                highest_score = (word, new_score)                
    return highest_score        
        
   
            



