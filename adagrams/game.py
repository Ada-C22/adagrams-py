import random

def draw_letters():
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

    weighted_list = []
    
    for letter, amount in LETTER_POOL.items():
	    weighted_list += letter * amount

    letters = []
    
    while len(letters) < 10:
        weighted_list_length = len(weighted_list)
        random_index = random.randrange(0,weighted_list_length)
        letters += weighted_list[random_index]
        weighted_list.pop(random_index)
        

    return letters
    
def uses_available_letters(word, letter_bank):
    word = word.upper()
    letters_in_word = ""

    for letter in letter_bank:
        if letter in word:
            letters_in_word += letter
    
    letters_in_word_list = list(letters_in_word)
    word_as_list = list(word)

    letters_in_word_list.sort()
    word_as_list.sort()

    if letters_in_word_list == word_as_list:
        return True
    else:
        return False


def score_word(word):
    word_score = 0
    word  = word.upper()

    for letter in word:
        if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U" or letter == "L" or letter == "N" or letter == "R" or letter == "S" or letter == "T":
            word_score += 1
        elif letter == "D" or letter == "G":
            word_score += 2
        elif letter == "B" or letter == "C" or letter == "M" or letter == "P":
            word_score += 3
        elif letter == "F" or letter == "H" or letter == "V" or letter == "W" or letter == "Y":
            word_score += 4
        elif letter == "K":
            word_score += 5
        elif letter == "J" or letter == "X":
            word_score += 8
        elif letter == "Q" or letter == "Z":
            word_score += 10

    if len(word) >= 7:
        word_score += 8

    return word_score


def get_highest_word_score(word_list):
    word_score_dict = {}
    high_score = ("", 0)

    for word in word_list:
        word_score_dict[word]= score_word(word)

    for word, score in word_score_dict.items():
        if score > high_score[1]:
            high_score = word,score
        elif score == high_score[1]:
            high_score += word, score
    if len(high_score) == 2:
        return high_score
    else:
        for word,score in word_score_dict.items():
            if len(word) == 10:
                high_score = word, score
                return high_score
        for word,score in word_score_dict.items():
            if len(word) == 2:
                high_score = word, score
                return high_score
        for word,score in word_score_dict.items():
            if len(word) == 3:
                high_score = word, score
                return high_score
        for word,score in word_score_dict.items():
            if len(word) == 4:
                high_score = word, score
                return high_score
        for word,score in word_score_dict.items():
            if len(word) == 5:
                high_score = word, score
                return high_score
        for word,score in word_score_dict.items():
            if len(word) == 6:
                high_score = word, score
                return high_score
        for word,score in word_score_dict.items():
            if len(word) == 7:
                high_score = word, score
                return high_score
        for word,score in word_score_dict.items():
            if len(word) == 8:
                high_score = word, score
                return high_score
        for word,score in word_score_dict.items():
            if len(word) == 9:
                high_score = word, score
                return high_score
        
        
        
    



    

    

                
                

    
    
