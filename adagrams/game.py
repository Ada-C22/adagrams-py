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

def draw_letters():
    #Create a set of 10 letters that matches the letter frequency distribution#
    draw = []
    letter_pool_copy = []

    #Calculate the weigths for each letter
    for letter, frequency in LETTER_POOL.items():
        weights = letter*frequency
        #add the weight letters to a new list
        for char in weights:
            letter_pool_copy.append(char)

    while len(draw) < 10:       
        #Take a random number within the len of letter pool and get the letter in that index
        random_letter = letter_pool_copy[random.randint(0,len(letter_pool_copy)-1)]
        
        #Check if the letter is still availabe in the letter pool and add it to the hand
        if random_letter in letter_pool_copy:
            draw.append(random_letter)
            
            #reduce the frequency in letter pool, for each letter added to the hand
            letter_pool_copy.remove(random_letter)
                
    return draw

def uses_available_letters(word, letter_bank):
    #check if the word is an anagram of some or all of the given letters in the hand

    casefold_word = word.casefold()
    letter_bank_copy = []

    #Ensure letter matching in letter_bank and word
    for letter in letter_bank:
        letter_bank_copy.append(letter.casefold())

    for char in casefold_word:
        #Take one of the letters from the hand and make unavailable in the bank copy
        if char in letter_bank_copy:
            letter_bank_copy.remove(char)
        else:
            return False

    return True

#-------- Score-Word Func Using Nested Lists --------#
SCORE_DICT = {  'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1, 'l': 1, 'n': 1, 'r': 1, 
                's': 1, 't': 1, 'd': 2, 'g': 2, 'b': 3, 'c': 3, 'm': 3, 'p': 3, 
                'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4, 'k': 5, 'j': 8, 'x': 8, 
                'q': 10, 'z': 10 }

def score_word(word):
    score = 0

    casefold_word = word.casefold()

    for letter in casefold_word:
        print (letter)
        score += SCORE_DICT.get(letter)

    if len(casefold_word) > 6:
        score += 8

    return score

def get_highest_word_score(word_list):
    #Calculate which word from the list has the highest score 
    # applying tie-breaking logic
    
    highest_score = 0
    highest_word = " "
    
    #calculate score for word in word_list
    for word in word_list:
        current_score = score_word(word) 
        
        #choose the word with highest score
        if current_score > highest_score:
            highest_word= word
            highest_score = current_score
        
        #If a tie and no word is 10 char, pick the shortest word 
        elif current_score == highest_score \
        and len(word) < len(highest_word) \
        and len(highest_word) != 10:
            highest_word = word

        #If a tie and one word is 10 char, pick that word
        elif len(word) == 10 \
        and len(highest_word) != 10:
            highest_word = word 

    return (highest_word, highest_score) 