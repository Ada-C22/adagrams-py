import random
import string

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
    hand =[]
    letter_frequncies={}
    for i in range(10):
        random_letter = random.choice(string.ascii_letters).upper()
        if random_letter not in hand:
            hand.append(random_letter)
            letter_frequncies[random_letter]=1
        else:
            if letter_frequncies[random_letter]< LETTER_POOL[random_letter]:
                hand.append(random_letter)
                letter_frequncies[random_letter] +=1
            else: 
                continue
    return hand

def uses_available_letters(word, letter_bank):
    letter_list = list(word.upper())
    letter_bank_freqs={}
    letter_list_freqs={}
    for letter in letter_bank:
            if letter not in letter_bank_freqs:
                letter_bank_freqs[letter] = 1
            else:
                letter_bank_freqs[letter] += 1
    for letter in letter_list:
        if letter not in letter_bank:
            return False
        else:
            if letter not in letter_list_freqs:
                letter_list_freqs[letter] = 1
            else:
                if letter_list_freqs[letter]>= letter_bank_freqs[letter]:
                    return False
                else:
                    letter_list_freqs[letter] += 1

    return True

def score_word(word):
    score = 0
    for letter in word:
        letter = letter.upper()
        if letter in ["A","E","I", "O", "U", "L", "N", "R","S","T"]:
            score += 1
        elif letter in ["D","G"]:
            score +=2
        elif letter in ["B","C","M","P"]:
            score += 3
        elif letter in ["F","H","V","W","Y"]:
            score += 4
        elif letter == "K":
            score += 5
        elif letter in ["J", "X"]:
            score += 8
        elif letter in ["Q","Z"]:
            score += 10
    if len(word)>= 7:
        score += 8
    return score

def get_highest_word_score(word_list):
    current_highest = [word_list[0], score_word(word_list[0])]
    for word in word_list:
        current_word_score= score_word(word)
        if current_word_score > current_highest[1] and len(current_highest[0])<10:
            current_highest[0] = word
            current_highest [1] = current_word_score 
        elif current_word_score == current_highest[1]:
            if len(current_highest[0]) == 10:
                continue
            elif len(word)==10 or len(word)< len(current_highest[0]):
                current_highest[0] = word
                current_highest [1] = current_word_score
    return tuple(current_highest)
    

