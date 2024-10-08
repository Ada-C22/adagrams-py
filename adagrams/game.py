import random

def draw_letters():
    '''
    The draw_letters function returns an array of 10 random uniquely selected letters from the pool of letters. 
    
    - On lines 15-17, the array pool_of_letters_array stores the letters and number of times it occurs.
    - On lines 19-25, letter_list is filled with 10 random uniquely selected letters and gets returned.
    '''

    LETTER_POOL = {
    'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1
}
    
    pool_of_letters_array = []
    for letter, frequency in LETTER_POOL.items(): 
        pool_of_letters_array += letter * frequency
    
    letter_list = []
    while len(letter_list) < 10:
        random_index = random.randint(0, len(pool_of_letters_array) - 1)
        letter_list.append(pool_of_letters_array[random_index])
        pool_of_letters_array.remove(pool_of_letters_array[random_index])

    return letter_list


def uses_available_letters(word, letter_bank):
    '''
    The uses_available_letters function will check if a word the player submits only uses letters that are in the letter_bank.

    - On lines 36-39, a frequency map is created to keep track of how many times a letter appears in the letter_bank.
    - On lines 41-48, we are checking if each letter in word appears in letter_frequency. If the letter is not in the frequency map or if the frequency is 0, a False value is returned; if the letter is in the frequency map, the frequency value is subtracted by 1 and a True value is returned.
    '''

    letter_frequency = {}

    for letter in letter_bank:
        letter_frequency[letter] = letter_frequency.get(letter, 0) + 1

    uppercase_word = word.upper()
    
    for letter in uppercase_word:
        if letter not in letter_frequency or letter_frequency[letter] == 0:
            return False
        letter_frequency[letter] -= 1

    return True


def score_word(word):
    '''
    The score_word function returns the score of the word using SCORE_CHART for points values

    - On lines 67-71, we are checking for characters in word to add to our points variable which has an initial value of 0. If there is a character that's not in the SCORE_CHART, it's added to the non_alpha_characters variable to keep track of it
    - On lines 73-76, we are checking if the length of the word is 7, 8, 9, or 10 to reward bonus points. If there were any non-alphabetic characters, it is subtracted from the length of the word to keep track of the true word length for the bonus points. After, the value of points is returned.
    '''
    
    SCORE_CHART = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
}
    
    BONUS_POINTS = 8
    points = 0
    non_alpha_characters = 0

    for character in word.upper():
        if SCORE_CHART.get(character):
            points += SCORE_CHART.get(character)
        else:
            non_alpha_characters += 1

    if (len(word) - non_alpha_characters) >= 7 and (len(word) - non_alpha_characters) <= 10:
        points += BONUS_POINTS

    return points


def get_highest_word_score(word_list):
    '''
    The get_highest_word_score function calculates scores for words and returns the winning word along with the score.

    - On lines 87-88, the highest_word is set to the 0th index of word_list and highest_score is the score of the 0th index of word_list as default values to be compared throughout the word_list. 
    - On lines 90-102, the current_score gets checked with highest_score and if current_score is greater than the highest_score, the highest_score is reassigned to the current_score. The highest_word is set to the word that is associated with the highest_score. The word with the highest score is returned as a tuple.
    '''
    
    highest_word = word_list[0]
    highest_score = score_word(word_list[0])

    for word in word_list[1::]:
        current_score = score_word(word)

        if current_score > highest_score:
            highest_score = current_score
            highest_word = word
        elif current_score == highest_score:
            if len(highest_word) == 10:
                continue
            elif (len(word) == 10) or (len(word) < len(highest_word)):
                highest_word = word

    return (highest_word, highest_score)