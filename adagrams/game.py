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
    letter_list = []
    
    # Create a list of letters, each letter appears according to their frequency
    for letter, letter_freq in LETTER_POOL.items():
        for i in range(letter_freq):
            letter_list.append(letter)
    

    #Create an empty letter_bank list, each letter will be append to letter_bank according to their random index. 
    #Using a while loop to control only ten letters with random indice will be added to letter_bank
    #If an index is used, it will be added to the set of indiced_used, so it will not be chosen again
    letter_bank = []
    indices_used = set()
    while len(letter_bank) < 10:
        index = random.randint(0, len(letter_list) - 1)
        if index not in indices_used:
            letter_bank.append(letter_list[index])
            indices_used.add(index)
        
    return letter_bank
    # AABCDEFGHZ -> {A:2 B:1 C:1 D:1 E:1 F:1 G:1 H:1 Z:1}
    

def uses_available_letters(word, letter_bank):
    letter_bank_dictionary = {}
    # convert letter bank into a map between letter and its frequency
    for letter in letter_bank:
        if letter not in letter_bank_dictionary:
            letter_bank_dictionary[letter]=1
        else:
            letter_bank_dictionary[letter]+=1
    # convert input to upper case 
    for letter in word.upper():
        if letter not in letter_bank_dictionary or letter_bank_dictionary[letter] == 0:
            return False
        else:
            letter_bank_dictionary[letter] -= 1
    return True

def score_word(word):
    total_scores = 0
    for letter in word.upper():
        scores = letter_values.get(letter, 0)
        total_scores += scores
    if len(word) > 6:
        total_scores += 8
    return total_scores

# create a dictionary of Letter and Value of points for each letter
letter_values = {
    'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
    'D': 2, 'G': 2,
    'B': 3, 'C': 3, 'M': 3, 'P': 3,
    'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
    'K': 5,
    'J': 8, 'X': 8,
    'Q': 10, 'Z': 10
}




def get_highest_word_score(word_list):
    best_word = ""
    highest_score = 0
    for word in word_list:
        score = score_word(word)
        
        #Choose the word with highest scores
        if score > highest_score:
            best_word = word
            highest_score = score
        elif score == highest_score:
            #if the word has 10 letters, it wins over the non-10-letter words.
            if len(word) == 10 and len(best_word) != 10:
                best_word = word
            #if all the words are non-10-letter words, the word with shortest length will win over the longer ones
            elif len(word) < len(best_word) and len(best_word) != 10:
                best_word = word
            #Python witll automatically return the first word in list, if there is a tie between words (same scores, same length)
            #This is naturally handled since the first word is not replaced! 

    return(best_word, highest_score)
    
 

"""
After several hands have been drawn, words have been submitted, checked, scored, and played, you need a way to find the highest scoring word. This function looks at the list of `word_list` and calculates which of these words has the highest score, applies any tie-breaking logic, and returns the winning word in a special data structure.

Implement a function called `get_highest_word_score` in `game.py`. This method should have the following properties:

- Has one parameter: `word_list`, which is a list of strings
- Returns a tuple that represents the data of a winning word and it's score.  The tuple must contain the following elements:
  - index 0 ([0]): a string of a word
  - index 1 ([1]): the score of that word
- In the case of tie in scores, use these tie-breaking rules:
    - prefer the word with the fewest letters...
    - ...unless one word has 10 letters. If the top score is tied between multiple words and one is 10 letters long, choose the one with 10 letters over the one with fewer tiles
    - If the there are multiple words that are the same score and the same length, pick the first one in the supplied list

"""