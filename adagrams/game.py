
LETTER_POOL = {
    1: {'A': 9},
    2: {'B': 2},
    3: {'C': 2},
    4: {'D': 4},
    5: {'E': 12},
    6: {'F': 2},
    7: {'G': 3},
    8: {'H': 2},
    9: {'I': 9},
    10: {'J': 1},
    11: {'K': 1},
    12: {'L': 4},
    13: {'M': 2},
    14: {'N': 6},
    15: {'O': 8},
    16: {'P': 2},
    17: {'Q': 1},
    18: {'R': 6},
    19: {'S': 4},
    20: {'T': 6},
    21: {'U': 4},
    22: {'V': 2},
    23: {'W': 2},
    24: {'X': 1},
    25: {'Y': 2},
    26: {'Z': 1}
}

SCORE_CHART = {
    1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
    2: ['D', 'G'],
    3: ['B', 'C', 'M', 'P'],
    4: ['F', 'H', 'V', 'W', 'Y'],
    5: ['K'],
    8: ['J', 'X'],
    10: ['Q', 'Z']
    }

def deep_copy_letter_pool(letter_pool):
    letter_pool_copy = {}
    for index, letters in letter_pool.items():
        letter_count = {}
        for letter, count in letters.items():
            letter_count[letter] = count
            letter_pool_copy[index] = letter_count
    return letter_pool_copy


def draw_letters():
    import random
    copy_pool = deep_copy_letter_pool(LETTER_POOL)
    hand = []
  
    while len(hand) < 10:
        letter_drawn = random.randint(1,26)
        letter_and_quantity = copy_pool[letter_drawn]
        for letter, quantity in letter_and_quantity.items():
            if quantity > 0:
                hand.append(letter)
                letter_and_quantity[letter] -= 1
    return hand


def deep_copy_letter_bank(letter_bank):
    letter_bank_copy = []
    for letter in letter_bank:
        letter_bank_copy += [letter]
    return letter_bank_copy


def uses_available_letters(word, letter_bank):
    
    copy_bank = deep_copy_letter_bank(letter_bank)
    word = word.upper()
    for letter in word:
        if letter in copy_bank:
            copy_bank.remove(letter)
        else:
            return False
    return True


def score_word(word):

    word = word.upper()
    total_score = 0
    
    if len(word) in range(7, 11):
        total_score += 8
    for letter in word:
        for score, letters in SCORE_CHART.items():
            if letter in letters:
                total_score += score
    return total_score

def word_score_list(word_list):
    score_chart = []
    for word in word_list:
        word_score = score_word(word)
        score_chart += [word_score]
    return score_chart


def get_highest_word_score(word_list):
   
    winning_word = None
    score_chart = word_score_list(word_list)
    highest_score = score_chart[0]

    for i in range(len(word_list)):
        if not winning_word:
            winning_word = word_list[i]
        elif score_chart[i] > highest_score:
            winning_word = word_list[i]
            highest_score = score_chart[i]
        elif score_chart[i] == highest_score:
            if len(word_list[i]) == 10 and len(winning_word) != 10:
                winning_word = word_list[i]
            elif len(winning_word) != 10 and len(word_list[i]) < len(winning_word):
                winning_word = word_list[i]
    return winning_word, highest_score
    







    
            
        

        
    

                                         

        
