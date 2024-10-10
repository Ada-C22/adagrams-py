
import random


def draw_letters():
    # array_of_strings = [ ]
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

    letter_pool = []
    for letter, count in LETTER_POOL.items():
        letter_pool.extend([letter] * count)
    
    hand = []
    
    for _ in range(10):
        random_index = random.randint(0, len(letter_pool) - 1)
        hand.append(letter_pool[random_index])
        letter_pool.pop(random_index)
    
    return hand





def uses_available_letters(word, letter_bank):

    word = word.upper()
    letter_bank_remaining = letter_bank.copy()

    for letter in word:
        if letter in letter_bank_remaining:
            letter_bank_remaining.remove(letter)
        else:
            return False
    return True

    


def score_word(word):

    # Define the letter scores
    score_chart = {
        'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
        'D': 2, 'G': 2,
        'B': 3, 'C': 3, 'M': 3, 'P': 3,
        'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
        'K': 5,
        'J': 8, 'X': 8,
        'Q': 10, 'Z': 10
    }
    
    # Initialize score to 0
    total_score = 0
    
    # Convert word to uppercase to handle case insensitivity
    word = word.upper()
    
    # Sum up the score for each letter
    for letter in word:
        total_score += score_chart.get(letter, 0)  # Add 0 if letter is not found (for safety)
    
    # Add bonus points if the word is 7-10 letters long
    if 7 <= len(word) <= 10:
        total_score += 8
    
    return total_score




def get_highest_word_score(word_list):
    # Initialize the best word and score
    best_word = None
    best_score = 0

    # Loop through each word in the list
    for word in word_list:
        # Get the score for the current word
        current_score = score_word(word)

        # Update best_word and best_score if conditions are met
        if (
            best_word is None or  # First word
            current_score > best_score or  # Higher score
            (
                current_score == best_score and len(word) == 10 and len(best_word) != 10  # Prefer 10-letter word
            ) or (
                current_score == best_score and len(word) < len(best_word) and len(best_word) != 10  # Prefer shorter word
            )
        ):
            best_word = word
            best_score = current_score

    # Return the word with the highest score
    return best_word, best_score

