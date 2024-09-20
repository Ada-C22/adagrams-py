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

    letter_bank_copy = letter_bank.copy()
    word = word.upper()  
    for char in word:
        #Take one of the letters from the hand and make unavailable in the bank copy
        if char in letter_bank_copy:
            letter_bank_copy.remove(char)
        else:
            return False

    return True

#-------- Score-Word Func Using Nested Lists --------#
SCORE_CHART = [
    [1,['A', 'E','I','O','U','L','N','R','S','T']],
    [2,['D','G']],
    [3,['B','C','M','P']],
    [4,['F','H','V','W','Y']],
    [5,['K']],
    [8,['J','X']],
    [10,['Q','Z']]
]
def score_word(word):
    #Returns the score of a given word as defined by the SCORE_CHART

    total_points = 0
    points = 0
    word = word.upper()
    for i in range(len(SCORE_CHART)):
        for char in word:
            if char in SCORE_CHART[i][1]: #check for char in each letter in list rows
                points =SCORE_CHART[i][0] #If found, access the index that has the score
                total_points += points
            else:
                points = 0

    #Extra points if word has 7 or more characters 
    if len(word) >= 7:
        total_points += 8
    
    return total_points

# #------Score_Word Func Using Dictionaries --------#
# SCORE_CHART = {
#     1:['A', 'E','I','O','U','L','N','R','S','T'],
#     2:['D','G'],
#     3:['B','C','M','P'],
#     4:['F','H','V','W','Y'],
#     5:['K'],
#     8:['J','X'],
#     10:['Q','Z']

# }
# def score_word(word):
#     #Returns the score of a given word as defined by the SCORE_CHART

#     points = 0
#     word = word.upper()

#     #access the lists in the dict (values)as letters
#     for score, letters in SCORE_CHART.items():
#         for i in range(len(letters)): 
#             for char in word:        
#                 if char in letters[i]: #check char in
#                     points += score    

#     #Extra points if word has 7 or more characters 
#     if len(word) >= 7:
#         points += 8

#     return points

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
        if current_score == highest_score \
        and len(word) < len(highest_word) \
        and len(highest_word) != 10:
            highest_word = word

        #If a tie and one word is 10 char, pick that word
        elif len(word) == 10 \
        and len(highest_word) != 10:
            highest_word = word 

    return (highest_word, highest_score) 