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
    '''
        Creates a comprehensive list of all instances of letters able to
        be selected from LETTER_POOL. Shuffles and return 10 randomly
        selected letters.
    '''

    letters_list = []
    num_letters = 10

    for letter, freq in LETTER_POOL.items():
        for i in range(freq):
            print(f"Iteration {i+1} of {freq} for letter {letter}")  # Debugging output
            print(f"Appending letter {letter} {freq} times")  # Debug output
            letters_list.append(letter)

    random.shuffle(letters_list)
    random_letters_list = letters_list[:num_letters]  # Select 3 elements

    return random_letters_list[:num_letters]


def uses_available_letters(word, letter_bank):
    '''
        
    '''
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass

print(draw_letters())