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
    
    hand_of_letters = []
    available_letters_list = []
    for letter, count in LETTER_POOL.items():
        for _ in range(count):
            available_letters_list.append(letter)

    while len(hand_of_letters) < 10: 
        
        letter_index = random.randint(0, len(available_letters_list) - 1)
        letter = available_letters_list[letter_index]
        hand_of_letters.append(letter)
        available_letters_list.pop(letter_index)
       
    return hand_of_letters





def uses_available_letters(word, letter_bank):
    letter_bank_copy = letter_bank [:]
    word = word.upper()
    for i in word:
        if i in letter_bank_copy:
            letter_bank_copy.remove(i)
        else:
            return False
    
    return True


def score_word(word):
    pass
    scores = {'A': 1, 
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
    score = 0
    word = word.upper()
    for i in word:
        if i in scores:
            score +=scores[i]
    
    if len(word) > 6 and len(word)<=10:
        score+=8
    return score
          
# def score_word(word):
#     scores = { 
#         1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
#         2: ["D", "G" ], 
#         3: ["B", "C", "M", "P" ], 
#         4: ["F", "H", "V", "W", "Y" ], 
#         5: ["K"], 
#         8: ["J", "X"],
#         10: ["Q", "Z" ] 
#     }

#     score = 0
#     word = word.upper()
#     for letter in word:
#         for number, letters in scores.items():
#             if letter in letters:
#                 score += number
#     if len(word) > 6:
#         score+=8
#     return score


def get_highest_word_score(word_list):
   
    winner = ("", 0)

    for word in word_list:
        score = score_word(word)
        if score > winner[1]:
            winner = (word, score)
            continue
        
        if score < winner[1] or len(winner[0]) == 10:
            continue
            
        if len(word) < len(winner[0]) or len(word) == 10:
            winner = (word, score)
    return winner






    