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
#generate list of letters to pull from:     
    letter_pool_list = []
    for letter, value in LETTER_POOL.items():
        for iteration in range(value):
            letter_pool_list.append(letter)

# find 10 letters with random choice from pool list
    ten_letter_list = []
    for i in range (10):
        range_end=len(letter_pool_list)-1
        random_index=random.randint(0,range_end)
        new_letter = letter_pool_list[random_index]
        ten_letter_list.append(new_letter)
        letter_pool_list.remove(new_letter)

    return ten_letter_list
    pass

def uses_available_letters(word, letter_bank):
    local_letter_bank = letter_bank[:]
    cap_word = word.upper()
    print(cap_word)
    
    for letter in cap_word:
        print(letter)
        if letter not in local_letter_bank:
            return False
        else: 
            local_letter_bank.remove(letter)

    return True


def score_word(word):
    letters_and_values = {
        #1 point
        "A" : 1, "E" : 1, "I" : 1, "O" : 1 , "U" : 1, "L" : 1, "N" : 1, "R" : 1, "S" : 1, "T" : 1,
        #2 points
        "D" : 2, "G" : 2,
        #3 points
        "B" : 3, "C" : 3, "M" : 3, "P" : 3,
        #4 points: 
        "F" : 4, "H" : 4, "V" : 4, "W" : 4, "Y": 4,
        #5 points: 
        "K" : 5,
        #6 points: 
        "J" : 8, "X" : 8,
        #7 points: 
        "Q" : 10, "Z" : 10
        }

    word_score = 0
    upper_word = word.upper()
    for letter in upper_word:
        letter_value = letters_and_values[letter]
        word_score += letter_value
# add 8 points to words that are over 7 letters. 
    if len(word) >= 7: 
        word_score += 8
    return word_score

def get_highest_word_score(word_list):
    winning_score = 0
    winning_str = ""
    for word in word_list:
        word_score = score_word(word)
        word_len = len(word)
#       compare scores/find first highest score & assign      
        if word_score  > winning_score: 
            winning_score = word_score
            winning_str = word
            winning_word_len = len(word)
#       Pick best highest score when score is tied. 
        elif word_score == winning_score: 
            if word_len == 10 and winning_word_len != 10:
                winning_score = word_score
                winning_str = word
                winning_word_len = word_len
            elif word_len < winning_word_len and winning_word_len != 10:
                winning_score = word_score
                winning_str = word
                winning_word_len = len(word)
#   generate best_word tuple.                 
    best_word = (winning_str, winning_score,)
    return best_word