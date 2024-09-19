import random

letter_pool = {
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
    """
    function to create a random hand of 10 letters
    no input
    output is a list of 10 random letters
    """ 
    # assign variable names to the letters and max usage num 
    letter_list, usage_list = list(letter_pool.keys()), list(letter_pool.values())
    
    hand = []
    while len(hand) < 10:
        position = random.randint(0, len(letter_list)-1)
        letter_frequency = usage_list[position] # assigns the random int to a usage number
        random_letter = letter_list[position] # assigns the random int to a letter
        
        if hand.count(random_letter) < letter_frequency:
            add_letter = hand.append(random_letter)
        else:
            continue
    return hand

def uses_available_letters(word, letter_bank):
    """
    function to check if a letter is in a list
    input is word (a string of letters), and letter bank (an array of words)
    output is return True if letter is in letter bank, or return False if letter is not in letter bank
    """ 
    # word = word.upper()
    # count = 0
    # for letter in word:
    #     if word.count(letter) > letter_bank.count(letter):
    #         return False
    #     elif letter in letter_bank:
    #         count += 1
    # if count == len(word):
    #     return True

    word = word.upper()
    list = []
    letter_bank_copy = letter_bank.copy()

    for each_letter in word:
        if each_letter in letter_bank_copy:
            list.append(each_letter)
            letter_bank_copy.remove(each_letter)
        else:
            return False
    return True

def score_word(word):
    """
    function calculates a score based on points for each letter and/or length of word and return score
    input word (string)
    output a score (int)
    """ 
    score_chart = {
        1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
        2: ['D', 'G'],
        3: ['B', 'C', 'M', 'P'],
        4: ['F', 'H', 'V', 'W', 'Y'],
        5: ['K'],
        8: ['J', 'X'],
        10: ['Q', 'Z']
    }
    word = word.upper()
    score = 0
    for letter in word:
        for point_value, letter_list in score_chart.items():
            if letter in letter_list:
                score += point_value

    if len(word) > 6:
        score += 8
    
    return score

def get_highest_word_score(word_list):
    """
    function determines word with highest score
    input is word list (list of words)
    output is a tuple of the winning word and its points
    """ 
    
    highest_value = 0
    highest_value_word = ""
    len_dict = {} # dict containing all words and its length
    word_length = 10


    for each_word in word_list:
        each_score = score_word(each_word) # assign score 

        if each_score > highest_value:
            len_dict = {}
            highest_value = each_score
            len_dict[each_word] = len(each_word)
        
        elif each_score == highest_value:
            len_dict[each_word] = len(each_word)

    for each_key, each_value in len_dict.items():

        # if the lenth of word is 10, chooses it or the first word
        if each_value == 10:
            highest_value_word = each_key
            break
        # picks the lowest length word
        elif each_value < word_length:
            word_length = each_value
            highest_value_word = each_key
            
    return highest_value_word, highest_value