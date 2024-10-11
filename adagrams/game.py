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
LETTER_SCORES = {
    'A': 1, 
    'B': 3, 
    'C': 3, 
    'D': 2, 
    'E': 1, 
    'F': 4, 
    'G': 2, 
    'H': 4, 
    'I': 1, 
    'J': 8, 
    'K': 5, 
    'L': 1, 
    'M': 3, 
    'N': 1, 
    'O': 1, 
    'P': 3, 
    'Q': 10, 
    'R': 1, 
    'S': 1, 
    'T': 1, 
    'U': 1, 
    'V': 4, 
    'W': 4, 
    'X': 8, 
    'Y': 4, 
    'Z': 10
}
HAND_SIZE = 10
BONUS_WORD_LEN = 7
BONUS_FOR_LONG_WORD = 8

def get_list_of_letters():
    # empty list where I would put all the correct amount of letters in.
    weighted_list = []

    # putting the data into list 
    for letter, amount in LETTER_POOL.items():
	    weighted_list += letter * amount

    return weighted_list

def draw_letters():
    weighted_list = get_list_of_letters()

    # letters is my "hand"
    letters = []
    
    # while the letters list's length is less than HAND_SIZE it will create a new random index 
    # and then add the letter that was at that index into letters list and remove from weighted list
    # so it cannot be chosen again

    while len(letters) < HAND_SIZE:
        weighted_list_length = len(weighted_list)
        random_index = random.randrange(0,weighted_list_length)
        letters.append(weighted_list[random_index])
        # weighted_list.pop(random_index)
        last_pos = len(weighted_list) - 1
        weighted_list[last_pos], weighted_list[random_index] = weighted_list[random_index], weighted_list[last_pos]
        weighted_list.pop()

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
        if letter not in letter_bank_copy:
            return False
        
        letter_bank_copy.remove(letter)
        
    # otherwise if letter is found in letter bank copy each time then return True
    return True

def add_bonus_points(word):
    bonus_points = 0
    if len(word) >= BONUS_WORD_LEN:
        bonus_points += BONUS_FOR_LONG_WORD
    return bonus_points

def score_word(word):
    # start word_score at 0 so I can add to it from there 
    word_score = 0

    # and make it upper case so its uniform
    word = word.upper()

    # for loop of letters in word to add appropriate score for each letter
    for letter in word:
        word_score += LETTER_SCORES[letter]

    # if letter over 7 characters then add additional 8 points 
    word_score += add_bonus_points(word)

    # return score
    return word_score

def get_word_score_dict(word_list):
    word_score_dict = {}
    for word in word_list:
        word_score_dict[word] = score_word(word)
    return word_score_dict

def tiebreaker(high_score_words, max_score):
    shortest_word = high_score_words[0]

    for word in high_score_words:
        if len(word) == 10:    
            return word, max_score
    for word in high_score_words:
        if len(word) < len(shortest_word):
            shortest_word = word
    return shortest_word, max_score

def get_highest_word_score(word_list):
    max_score = 0
    high_score_words = []
    
    word_score_dict = get_word_score_dict(word_list)

    for word, score in word_score_dict.items():
        if score > max_score:
            max_score = score
            high_score_words = [word]
        elif score == max_score:
            high_score_words.append(word)

    if len(high_score_words) == 1:
        return high_score_words[0], max_score
    else:
        return tiebreaker(high_score_words, max_score)