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

    # empty list where I would put all the correct amount of letters in.
    weighted_list = []

    # putting the data into list 
    for letter, amount in LETTER_POOL.items():
	    weighted_list += letter * amount

    # letters is my "hand"
    letters = []
    
    # while the letters list's length is less than 10 it will create a new random index 
    # and then add the letter that was at that index into letters list and remove from weighted list
    #  so it cannot be chosen again

    while len(letters) < 10:
        weighted_list_length = len(weighted_list)
        random_index = random.randrange(0,weighted_list_length)
        letters += weighted_list[random_index]
        weighted_list.pop(random_index)

    # return list of letters
    return letters
    
def uses_available_letters(word, letter_bank):
    # take the word and change it to upper case so it matches the letter bank letters
    word = word.upper()
    # made a copy of letter that would not change the original
    letter_bank_copy = letter_bank[:]

    # check for each letter in the word if its in the letter_bank_copy and
    # remove it from the letter_bank_copy so that it can account for multiples
    # if at any point the letter is not there then returns False
    for letter in word:
        if letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
        else: 
            return False
        
    # otherwise if letter is found in letter bank copy each time then return True
    return True

def score_word(word):
    # start word_score at 0 so I can add to it from there 
    word_score = 0

    # and make it upper case so its uniform
    word = word.upper()

    # for loop of letters in word to add appropriate score for each letter
    for letter in word:
        if letter in ["A","E","I","O","U","L", "N","R","S", "T"]:
            word_score += 1
        elif letter in ["D","G"]:
            word_score += 2
        elif letter in ["B", "C", "M","P"]:
            word_score += 3
        elif letter in ["F","H","V","W","Y"]:
            word_score += 4
        elif letter in ["K"]:
            word_score += 5
        elif letter in ["J","X"]:
            word_score += 8
        elif letter in ["Q","Z"]:
            word_score += 10

    # if letter over 7 characters then add additional 8 points
    if len(word) >= 7:
        word_score += 8

    # return score
    return word_score

def get_highest_word_score(word_list):
    # empty list to get dictionary of word score so I can loop through it later
    word_score_dict = {}

    # tuple of high_score to return later
    high_score = ("", 0)

    # getting the score of each word again
    for word in word_list:
        word_score_dict[word]= score_word(word)
    # for each score in dict if the score is higher than the score already there
    # then replace it, if its the same then add it to high_score
    for word, score in word_score_dict.items():
        if score > high_score[1]:
            high_score = word,score
        elif score == high_score[1]:
            high_score += word, score

    # if only one set of info(word, score) in high_score then return high_score
    if len(high_score) == 2:
        return high_score
    
    # otherwise if more than one set of high_score so theres a tie then continue
    else:
        # empty high_score dict so I can iterate over it later
        high_score_dict = {}

        # put together dictionary of high scores to compare
        for i in range(0, len(high_score),2):
            word = high_score[i]
            score = high_score[i+1]
            high_score_dict[word] = score

        # loop through to check for a word that has length 10 and return high score
        for word,score in high_score_dict.items():
            if len(word) == 10:
                return word,score
            
        # then if no words with length 10 then loop for length in range 2-9 and return high score
        for length in range(2,10):
            for word,score in high_score_dict.items():
                if len(word) == length:
                    return word,score