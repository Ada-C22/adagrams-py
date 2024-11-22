import random

def draw_letters():
    list_letters = []
    distribution_of_letters = {
        "A":9,
        "B":2,
        "C":2,
        "D":4,
        "E":12,
        "F":2,
        "G":3,
        "H":2,
        "I":9,
        "J":1,
        "K":1,
        "L":4,
        "M":2,
        "N":6,
        "O":8,
        "P":2,
        "Q":1,
        "R":6,
        "S":4,
        "T":6,
        "U":4,
        "V":2,
        "W":2,
        "X":1,
        "Y":2,
        "Z":1
    }


    list_letters = []
    
    while len(list_letters) != 10:
        letters = list(distribution_of_letters.keys())
        random_letter = random.choice(letters)
        value = distribution_of_letters[random_letter]
        if value > 0:
            distribution_of_letters[random_letter] = value -1
            list_letters.append(random_letter)

    return list_letters

def uses_available_letters(word, letter_bank):
    word = word.upper()
    letters_copy = letter_bank[:]
    for letter in word:
        if letter in letters_copy:
            letters_copy.remove(letter)    
        else:
            return False
    return True

def score_word(word):
    score = {
        "A" : 1,
        "E" : 1,
        "I" : 1,
        "O" : 1,
        "U" : 1,
        "L" : 1,
        "N" : 1,
        "R" : 1,
        "S" : 1,
        "T" : 1,
        "D" : 2,
        "G" : 2,
        "B" : 3,
        "C" : 3,
        "M" : 3,
        "P" : 3,
        "F" : 4,
        "H" : 4,
        "V" : 4,
        "W" : 4,
        "Y" : 4,
        "K" : 5,
        "J" : 8,
        "X" : 8,
        "Q" :10,
        "Z" :10
    }
    total_score = 0
    word = word.upper()
    for letter in word:
        value = score.get(letter, 0)
        total_score += value
    if len(word) >= 7 and len(word) <= 10 :
            total_score += 8
            
    return total_score


def get_highest_word_score(word_list):
    highest_word = ""
    highest_score = 0
    for word in word_list:
        word_score = score_word(word)
        if word_score > highest_score:
            highest_score = word_score
            highest_word = word
        elif word_score == highest_score:
            if len(highest_word) == 10:
                continue
            elif len(word)== 10:
                highest_word = word
            elif len(word)<len(highest_word):
                highest_word = word 
    return(highest_word,highest_score)





        





















    