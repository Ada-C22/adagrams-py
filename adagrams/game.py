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

SCORE_CHART = {
    ('A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'): 1,
    ('D', 'G'): 2,
    ('B', 'C', 'M', 'P'): 3,
    ('F', 'H', 'V', 'W', 'Y'): 4,
    ('K',): 5,
    ('J', 'X'): 8,
    ('Q', 'Z'): 10
}
def create_letter_pool_list():
    '''returns a total list of letters from LetterPool'''
    letter_pool_list = []
    for letter, freq in LETTER_POOL.items():
        for i in range(freq):
            letter_pool_list.append(letter)
    return letter_pool_list 

def count_letters(list, letter):
    '''returns the count of a letter in a list'''
    count = 0
    for item in list:
        if item == letter:
            count += 1
    return count

def draw_letters():
    '''returns a list of 10 random letters from LetterPool'''
    letter_pool_list = create_letter_pool_list()
    letter_bank = []

    while len(letter_bank) < 10: 
        random_num = random.randint(0, 97)
        letter = letter_pool_list[random_num] 
        letter_count = count_letters(letter_bank, letter) 
        
        if letter_count >= LETTER_POOL[letter]:
            continue 
        else:
            letter_bank.append(letter)
            
    return letter_bank

def uses_available_letters(word, letter_bank):
    '''returns true if the word uses available letters'''
    word = word.upper()
    is_valid_word = True
    for letter in word: 
        letter_in_word_count = count_letters(word, letter) 
        letter_in_bank_count = count_letters(letter_bank, letter)
        if letter_in_word_count > letter_in_bank_count:
            is_valid_word = False
        elif letter not in letter_bank:
            is_valid_word = False
    return is_valid_word


def score_word(word):
    '''returns the score of the word'''
    word = word.upper()
    score = 0
    for letter in word: 
        for letter_point, point in SCORE_CHART.items():
            if letter in letter_point: 
                score += point
    if len(word) >= 7: 
        score += 8
    return score

def get_highest_word_score(word_list):
    '''returns the word with the highest score from word_list'''
    winning_word = ""
    word_len = len(word_list[-1])
    max_score = score_word(word_list[-1])
        
    for word in word_list: 

        if score_word(word) > max_score: 
            max_score = score_word(word)
            winning_word = word
        elif score_word(word) == max_score:
            if len(word) == 10:
                max_score = score_word(word)
                winning_word = word
                word_len = len(word) 
                break
            elif len(word) == word_len:
                max_score = score_word(word)
                winning_word = word
                word_len = len(word)
            elif len(word) < word_len:
                max_score = score_word(word)
                winning_word = word
                word_len = len(word)                     

    return winning_word, max_score

print(get_highest_word_score(["AAAAAAAAAA", "BBBBBB"]))
