import random

def draw_letters():
    # define the dictionary with the letters and their value
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

    def pick_random_letter():
        # choose a letter randomly from the dict
        letters = [letter for letter, value in LETTER_POOL.items() if value > 0] # looping through LETTER_POOL to get the value of the letters only if the value is bigger than 0
        if not letters:
            return None    #if there are no available letters, return None
        # use random.randint to pick a letter by index
        index = random.randint(0, len(letters) - 1)        # generates a random index between 0 and len(letters) - 1
        return letters[index]
    
    draw_letters = []

    for i in range(10):    #select exactly 10 letters from dict
        letter = pick_random_letter()
        if letter is None:         # if None is returned indicating no more letters available, break the loop
            break
        draw_letters.append(letter)    # adding the randomly picked letters into the initial empty list
        LETTER_POOL[letter] -= 1       # decrease the count of the drawn letter in the dict
        if LETTER_POOL[letter] == 0:   # if the count of a letter reaches 0, removes the letter from the dict
            del LETTER_POOL[letter] # remove the letter if its value reaches 0

    return draw_letters

result = draw_letters()

def uses_available_letters(word, letter_bank):
    # function that counts each letters that occured in the list of letters 
    # this part of the code can be replaced by import counter
    def count_letters(letters):
        counts = {}
        for letter in letters:
            if letter in counts:
                counts[letter] += 1
            else:
                counts[letter] = 1
        return counts
    
    # convert word and letter_bank to lowercase to handle case sensitiveness
    word = word.lower()
    letter_bank = [letter.lower() for letter in letter_bank]
    
    # count the frequencies of the letters in word and letter_bank (word represents the user input words and letter_bank represent the letters that have been drawn)
    word_counts = count_letters(word)
    letter_bank_counts = count_letters(letter_bank)

    # check to see if every letters in word is available in letter_bank
    for letter, count in word_counts.items():
        if letter_bank_counts.get(letter, 0) < count:
            return False           # if the letter count in word is more than what we have in letter_bank
    return True                    # if all the letters are available in letter_bank   


def score_word(word):
    # score map, value of each letters
    letter_scores = {
        'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1,
        'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
        'D': 2, 'G': 2,
        'B': 3, 'C': 3, 'M': 3, 'P': 3,
        'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
        'K': 5,
        'J': 8, 'X': 8,
        'Q': 10, 'Z': 10
    }
    # convert the word to uppercase to match the key in letter_score
    word = word.upper()
    # initialize base score
    base_score = 0
    for letter in word:
        base_score += letter_scores.get(letter, 0)

    # calculate the bonus points for the words od length 7 or more
    if len(word) >= 7:
        bonus_points = 8
    else: 
        bonus_points = 0

    total_score = base_score + bonus_points

    return total_score


def get_highest_word_score(word_list):
    highest_word = ""
    highest_score = 0

# loop through the word_list to get the score
    for word in word_list: 
        score = score_word(word)

        if score > highest_score:
            highest_word = word
            highest_score = score
        # check if current word's score is equal to the highest score.
        elif score == highest_score:
            # check if the current word has 10 characters, it will replacw the previous highest word
            if len(word) == 10 and len(highest_word) != 10:
                highest_word = word
            # if the current word has less characters it will replace the previous highest word
            elif len(word) < len(highest_word) and len(highest_word) != 10:
                highest_word = word
            # assign current word to highest word if the lengths of the current word and highest word are the same
            elif len(word) == len(highest_word) and highest_word == "":
                highest_word = word

    return (highest_word, highest_score)

        



    

