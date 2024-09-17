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
    # Create empty list to store choosen letters
    hand = []
    # Create a complete pool of letter options
    weighted_letter_pool = []
    for letter, freq in LETTER_POOL.items():
        # Add the letter to the pool as many times as its frequency value
        for _ in range(freq):
            weighted_letter_pool.append(letter)
    # Randonly choose letters for hand ()
    while len(hand) < 10:
        random_index = random.randint(0, len(weighted_letter_pool)-1)
        random_letter = weighted_letter_pool[random_index]
        # Add letter to hand
        hand.append(random_letter)
        # Remove picked letter from pool
        weighted_letter_pool.pop(random_index)
    return hand

def uses_available_letters(word, letter_bank):
    # Change word to uppercase
    word = word.upper()
    # Create a dictionary of the frequency of letters in letter_bank
    max_letter_freqs = {}
    for letter in letter_bank:
            if letter not in max_letter_freqs:
                max_letter_freqs[letter] = 1
            else:
                max_letter_freqs[letter] += 1
    # Create dictionary to track the number of times a lettr is used in a word
    letter_use_freqs = {}
    # Check if the word is in the letter_bank
    for letter in word:
        if letter not in letter_bank:
            return False
        # Check if letter is in letter_use_freqs
        if letter not in letter_use_freqs:
            # Create entry if not
            letter_use_freqs[letter] = 1
        else:
            # If the letter usage hasn't reached it's maximum frequncy, allow it
            if letter_use_freqs[letter]< max_letter_freqs[letter]:
                letter_use_freqs[letter] += 1
            else:
                # if the letter has already reached it's maximum frequency, return False
                return False

    return True

def score_word(word):
    # Create score tracking variable
    score = 0
    # Add the corresponding score for each letter
    for letter in word:
        letter = letter.upper()
        if letter in ["A","E","I", "O", "U", "L", "N", "R","S","T"]:
            score += 1
        elif letter in ["D","G"]:
            score += 2
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
    # Add 8 point bonus for words longer than 7 letters
    if len(word) >= 7:
        score += 8
    return score

def get_highest_word_score(word_list):
    # Create a variable to hold the word with hightest score
    highest_score = {"word": "", "score":0}
    # Iterate throught the word_list
    for word in word_list:
        # Score the word
        current_word_score = score_word(word)
        # Replace highest_score values  if the current_word_score is higher
        if current_word_score > highest_score["score"]:
            highest_score["word"] = word
            highest_score ["score"] = current_word_score 
        # Tie-breakers
        elif current_word_score == highest_score["score"]:
            # Keep the highest_score if it is ten letters long
            if len(highest_score["word"]) == 10:
                continue
            # Replace highest_score if the current_word is ten letters or shorter than the highest_score 
            elif len(word) == 10 or len(word) < len(highest_score["word"]):
                highest_score["word"] = word
                highest_score ["score"] = current_word_score
    return tuple([highest_score["word"], highest_score["score"]])
    

