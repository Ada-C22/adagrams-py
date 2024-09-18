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
    import random 
    build an array (a hand) of 10 string
    a letter randomly draw from that pool
    """ 
    
    # give variable names to the letters and max usage num 
    letter_list, usage_list = list(letter_pool.keys()), list(letter_pool.values())
    
    # generate a random letter
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
    word = word.upper()
    count = 0
    for letter in word:
        if word.count(letter) > letter_bank.count(letter):
            return False
        elif letter in letter_bank:
            count += 1
    if count == len(word):
        return True

def score_word(word):
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

words = ["X", "XX", "XXX", "XXXX"]
def get_highest_word_score(word_list):
    
    score_dict = {}
    highest_value = 0
    highest_value_word = ""

    for each_word in word_list:
        score = score_word(each_word)
        score_dict[each_word] = score
        if score > highest_value:
            highest_value = score
            highest_value_word = each_word

    print(highest_value_word)
    print(highest_value)
    return highest_value_word, highest_value

    # for each_word, each_value in score_dict.items():
    #     for each in each_value:

get_highest_word_score(words)