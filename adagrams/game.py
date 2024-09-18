import random

NUM_DRAWN = 10

def draw_letters():
    '''
    Creates a list of specific length. Elements of the list are randomly
    selected letters from a pool defined within the function.

    Returns:
        letters_drawn (list): random letters in a list of X length

    '''
    letters_drawn = []
    letter_pool = build_letter_pool()

    for _ in range(NUM_DRAWN):
        random_index = random.randint(0, len(letter_pool) - 1)
        selected_letter = letter_pool[random_index]

        letters_drawn.append(selected_letter)
        letter_pool.remove(selected_letter)
    
    return letters_drawn

def uses_available_letters(word, letter_bank):
    '''
    Determines if a given word can be spelled using only letters from
    the letter bank.

    Checks whether each letter in the word is found in the letter bank,
    removing letters as they are found.

    Parameters:
        word (str): The word to be checked.
        letter_bank (list): List of letters available to form words.

    Returns:
        bool: True if the given word can be made using only the letters
        available in letter_bank, otherwise False
    '''
    copied_list = []

    for letter in letter_bank:
        copied_list.append(letter)

    for letter in word.upper():
        if letter in copied_list:
            copied_list.remove(letter)
        else:
            return False

    return True

def score_word(word):
    '''
    Calculates the total score of the given word based on letter values.

    Each letter has a specific assigned point value. The total score is
    the sum of these values. Words of a minimum length receive an 
    additional bonus.
    
    Parameters:
        word (str): The word to be scored.

    Returns:
        total_score (int): The total score for the word, including any
        applicable bonuses.
    '''
    POINT_VALUES  = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 
    'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 
    'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 
    'Y': 4, 'Z': 10
}
    BONUS_LENGTH = 7
    BONUS_POINTS = 8

    total_score = sum(POINT_VALUES.get(letter.upper(), 0) for letter in word)
    
    if len(word) >= BONUS_LENGTH:
        total_score += BONUS_POINTS

    return total_score
        
def get_highest_word_score(word_list):
    '''
    Finds and returns the highest-scoring word in the provided list of
    words.

    Compares the scores of each word and applies tie-breaking rules if
    multiple words have the same score. Calls the tie_breaker helper
    function if there is a tie. Returns the winning word and its
    score.

    Parameters:
        word_list (list): A list of words to score and compare.

    Returns:
        tuple: Contains the highest-scoring word and its score.
    '''
    winning_word = None
    highest_score = 0

    for word in word_list:
        word_score = score_word(word)

        if winning_word is None or word_score > highest_score:
            winning_word = word
            highest_score = word_score
        elif word_score == highest_score:
            winning_word = tie_breaker(word, winning_word)

        if is_max_length(winning_word):
            break

    return (winning_word, highest_score)

def build_letter_pool():
    '''
    Builds and returns a list of letters repeated according to its 
    frequency as defined in the LETTER_POOL dictionary.

    Returns:
        list: A list of letters populated at their defined frequencies.
    '''
    LETTER_POOL = {
        'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 
        'I': 9, 'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 
        'Q': 1, 'R': 6, 'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 
        'Y': 2, 'Z': 1
    }

    return [letter for letter, freq in LETTER_POOL.items() for _ in range(freq)]

def tie_breaker(word, current_winner):
    '''
    Determines the winning word in case of a tied score.

    Preference is given to words of maximum length in their order of
    appearance. If neither word is of maximum length, the word with the
    fewest letters will be selected as the winner.

    Parameters:
        word (str): A word being compared for a tie.
        current_winner (str): The current winning word.
    
    Returns:
        current_winner (str): The word that wins in tie-breaking logic.
    '''
    if is_max_length(current_winner):
        return current_winner
    if is_max_length(word) or len(word) < len(current_winner):
        return word

    return current_winner

def is_max_length(word):
    '''
    Checks to see if the word has the maximum possible length.

    Parameters:
        word (str): The word to check.

    Returns:
        bool: True if the word is of max length, otherwise False.
    '''
    return len(word) == NUM_DRAWN