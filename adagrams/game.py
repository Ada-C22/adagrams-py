import random
import pytest

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
    # build a hand_letter_list
    letter_list = []
    # turning LETTER_POOL dictionary into a list
    for letter, count in LETTER_POOL.items():
        letter_list += [letter] * count
    # build a hand of letters list
    hand_card = []
    for i in range(10):
        index = random.randint(0,len(letter_list)-1)
        hand_card.append(letter_list[index])
        letter_list.pop(index) 

    return hand_card


def uses_available_letters(word, letter_bank):
    word = word.upper()
    word_count = {}
    letter_bank_count = {}
    # count how many string in word and build dict
    for i in word:
        if i in word_count:
            word_count[i] += 1
        else:
            word_count[i] = 1

    # count how many string in letter_bank and build dict
    for y in letter_bank:
        if y in letter_bank_count:
            letter_bank_count[y] += 1
        else:
            letter_bank_count[y] = 1

    # compare word_count and letter_bank_count
    for key in word_count:
        if key not in letter_bank_count or \
            word_count[key] > letter_bank_count[key]:
            return False
    
    return True


def score_word(word):
    # bulid dict of score
    score_dict = {
        'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
        'D': 2, 'G': 2,
        'B': 3, 'C': 3, 'M': 3, 'P': 3,
        'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
        'K': 5,
        'J': 8, 'X': 8,
        'Q': 10, 'Z': 10
    }
    # input is empty
    if word == "":
        return 0
    # check each vlaue of letter
    word = word.upper()
    score_count = []
    for letter in word:
        score = score_dict.get(letter,0)
        score_count.append(score)
    total_score = sum(score_count)

    if 7 <= len(word) <= 10:
        total_score += 8

    return total_score 


    # more than 7, 8, 9, or 10 gets an additional 8 points
    # return total score



def get_highest_word_score(word_list):
    # defind
    max_score = 0
    word = None
    # get the highest score
    for i in word_list:
        score = score_word(i)
        if score > max_score:
            word = i
            max_score = score

        # same score compare
        elif score == max_score:
            if len(i) == 10 and len(word) != 10:
                word = i
            elif len(i) < len(word) and len(i) != 10 and len(word) != 10:
                word = i

    # return tuple
    return (word, max_score)