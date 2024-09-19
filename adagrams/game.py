import random

letter_counts = {
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

# No parameters
# Returns an array of ten strings
# Each string should contain exactly one letter
# These represent the hand of letters that the player has drawn
# The letters should be randomly drawn from a pool of letters
# This letter pool should reflect the distribution of letters as described in the table below
# There are only 2 available C letters, so draw_letters cannot ever return more than 2 Cs
# Since there are 12 Es but only 1 Z, it should be 12 times as likely for the user to draw an E as a Z
# Invoking this function should not change the pool of letters
# Imagine that the user returns their hand to the pool before drawing new letters
def draw_letters():
    all_letters = []
    hand= []
    for key in letter_counts:
        for num in range(0, letter_counts[key]):
            all_letters.append(key)
    for pepar in range(0, 10):
        random.shuffle(all_letters)
        random_index = random.randint(0, len(all_letters)-1)
        hand.append(all_letters[random_index])
    return hand


def uses_available_letters(word, letter_bank):
    word = word.upper()
    for char in word:
        if char not in letter_bank:
                return False
        if word.count(char) > letter_bank.count(char):
            return False
    return True


# Wave 3: score_word
# Now you need a function returns the score of a given word as defined by the Adagrams game.
#
# Implement the function score_word in game.py. This method should have the following properties:
#
# Has one parameter: word, which is a string of characters
# Returns an integer representing the number of points
# Each letter within word has a point value. The number of points of each letter is summed up to represent the total score of word
# Each letter's point value is described in the table below
# If the length of the word is 7, 8, 9, or 10, then the word gets an additional 8 points
def score_word(word):
    pass




def get_highest_word_score(word_list):
    pass