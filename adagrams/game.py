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
    letters_in_hand = []
    letters_list = []
    count = 0

    for letter in LETTER_POOL:
        for value in range(LETTER_POOL[letter]):
            letters_list.append(letter)

    print(f"len(letters_list) before = {len(letters_list)}")
    print(f"letters_list before = {letters_list}")

    while count < 10:
        random_letter_index = random.randint(0, len(letters_list))
        letters_in_hand.append(letters_list[random_letter_index])
        letters_list.pop(random_letter_index)
        count += 1

    print(f"len(letters_list) after = {len(letters_list)}")
    print(f"letters_list after = {letters_list}")
    print(f"letters_in_hand = {letters_in_hand}")

    return letters_in_hand
      
   

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass