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

    # Create an empty list to hold the letters from LETTER_POOL 
    letter_list = []

    # Go through each letter and its quantities in the letter pool
    for letter, quantity in LETTER_POOL.items():
        # Add the letter to the list, repeating according to its quantity
        letter_list.extend([letter]*quantity)
    
    # Create another empty list for the letter that will be drawn
    hand_of_ten_letters = []

    # Choose 10 letters
    for _ in range(10):
        # Select a random index in the list
        index = random.randint(0, len(letter_list)-1)
        # Add the letter at the index to the list of drawn letters
        hand_of_ten_letters.append(letter_list[index])
        # Remove that letter from the list so we don't choose it again
        letter_list.pop(index)

    # Return the 10 drawn letters   
    return hand_of_ten_letters

def uses_available_letters(word, letter_bank):

    # Covert all letters to uppercase
    word = word.upper()
    letter_bank = [letter.upper() for letter in letter_bank]
    
    # Create an empty dictionary to count the letters in the letter bank
    available_letters = {}
    for letter in letter_bank:
        if letter in available_letters:
            available_letters[letter] += 1
        else:
            available_letters[letter] = 1
    
    # Check if every letter in the word is available in the letter bank and has the required quantitiy
    for letter in word:
        if letter in available_letters and available_letters[letter] > 0:
            available_letters[letter] -= 1
        else:
            return False
    
    return True


def score_word(word):

    # Create a dictionary based on the score chart
    letter_values = {
        'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1, 'D': 2, 'G': 2, 'B': 3, 'C': 3, 'M': 3, 'P': 3, 
        'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4, 'K': 5, 'J': 8, 'X': 8, 'Q': 10, 'Z': 10
    }

    # Covert the word to upper case
    word = word.upper()
    total_score = 0

    # Calcualte the base score
    for letter in word:
        if letter in letter_values:
            total_score += letter_values[letter]
    
    # Add bonus pointsif the world lenght is equal or greater to 7
    if len(word) >=7:
        total_score += 8
    
    return total_score

def get_highest_word_score(word_list):
    highest_word = ""
    highest_score = 0

    for word in word_list:
        # Get the score of the current word
        score = score_word(word)

        # If this score is higher than what we've got
        if score > highest_score:
            #Update the best word
            highest_word = word
            # Update the best score
            highest_score = score
        elif score == highest_score:
            # Prefer the ten letter word if available
            if len(word) == 10 and len(highest_word) != 10:
                highest_word = word
            # Prefer the shorter word if they are the same score
            elif len(word) < len(highest_word) and len(highest_word) <10:
                highest_word = word
            # If both are the same lenght, choose the one that shows first in the list
            elif len(word) == len(highest_word):
                # Do nothing and keep the current highest word
                continue

    return (highest_word, highest_score)