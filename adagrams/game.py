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
    draw = []
    letter_pool_copy = LETTER_POOL.copy()
    #Place the key values (letters) into a list to be able to acces indexes
    letters_list = list(letter_pool_copy.keys())
    while len(draw) < 10:
        #Take a random number and get the letter in that index
        random_letter = letters_list[random.randint(0,len(letter_pool_copy)-1)]
        #Check if the letter is availabe in the letter pool and add it to the hand
        if letter_pool_copy[random_letter] >= 1:
            draw.append(random_letter)
            #reduce the frequency in lettr pool, for each letter added to the hand
            letter_pool_copy[random_letter] -= 1         
    return draw

def uses_available_letters(word, letter_bank):
    # char_frequency = {}

    # letter_bank_copy = letter_bank.copy()
    # word = word.upper()
    
    # while True:
    #     for char in word:
    #         if char in letter_bank_copy:
    #             letter_bank_copy.remove(char)
    #         else:
    #             return False
    # return True

    letter_bank_frequency = {}
    word_frequency = {}
    word = word.upper()
    #create the dicts with  letter and frequencies
    
    for letter in letter_bank:
        if letter in letter_bank_frequency:
            letter_bank_frequency[letter] += 1
        else:
            letter_bank_frequency[letter]=1
    if word:
        for word_letter in word:
            if word_letter in word_frequency:
                word_frequency[word_letter] +=1
            else:
                word_frequency[word_letter] = 1
    #Compare the dicts values giving a key
    for char in word:
        if word_frequency[char] > letter_bank_frequency.get(char,0):
            return False
    return True

# score_chart = {
#     1:['A', 'E','I','O','U','L','N','R','S','T'],
#     2:['D','G'],
#     3:['B','C','M','P'],
#     4:['F','H','V','W','Y'],
#     5:['K'],
#     8:['J','X'],
#     10:['Q','Z']
# }
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
    total_points = 0
    points = 0
    word = word.upper()
    for i in range(len(SCORE_CHART)-1):
        for score_letters_list in SCORE_CHART[i][1]:
            for char in word:
                if char in score_letters_list:
                    points =SCORE_CHART[i][0]
                    total_points += points
                else:
                    points = 0
                    
    if len(word) >= 7:
        total_points += 8
    
    return total_points




def get_highest_word_score(word_list):
    pass