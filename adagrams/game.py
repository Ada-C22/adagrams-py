import random

def draw_letters():
   Letter_POOL = {
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
   #taking an empty list to store drawn letters
   drawn_letters =[]
   total_letters = sum(Letter_POOL.values())

   HAND_SIZE = 10
   while len(drawn_letters) < HAND_SIZE:
        # Generating a random number between 1 and the total number of letters
        rand_index = random.randint(1, total_letters)

        # Finding  the corresponding letter
        cumulative_count = 0
        for letter, frequency in Letter_POOL.items():
            cumulative_count += frequency
            if rand_index <= cumulative_count:
                drawn_letters.append(letter)
                Letter_POOL[letter] -= 1
                total_letters -= 1
                break

   return drawn_letters


def uses_available_letters(word, letter_bank):

#    converting all the letters in letter bank to upper case
    letter_bank = [letter.upper() for letter in letter_bank]
# making a dictionary for a letter_bank to check the frequency of letters
    letter_frequency_dict = {}
    for letter in letter_bank:
        if letter in letter_frequency_dict:
            letter_frequency_dict[letter] += 1
        else:
            letter_frequency_dict[letter] = 1
    #converting all the letters of word into uppercase and checking the frequebcy of the letter, if found decrementing the value or else returning false

    for letter in word.upper():
        if letter not in letter_frequency_dict or letter_frequency_dict[letter] == 0:
            return False
        else:
            letter_frequency_dict[letter] -= 1
    return True

def score_word(word):
    LETTER_SCORES = {
        'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
        'D': 2, 'G': 2,
        'B': 3, 'C': 3, 'M': 3, 'P': 3,
        'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
        'K': 5,
        'J': 8, 'X': 8,
        'Q': 10, 'Z': 10
    }
    word = word.upper()
    total_score = 0

    total_score += sum(LETTER_SCORES.get(letter, 0) for letter in word )

    BONUS_LENGTH_MIN = 7
    BONUS_LENGTH_MAX = 10
    BONUS_POINTS = 8

    if BONUS_LENGTH_MIN <= len(word) <= BONUS_LENGTH_MAX:
        total_score += BONUS_POINTS

    return total_score


def get_highest_word_score(word_list):
    max_word = word_list[0]
    max_word_score = score_word(max_word)
    #iterating from the second word
    for word in word_list[1:]:
        word_score = score_word(word)
        if word_score > max_word_score:
            max_word = word
            max_word_score = word_score

        # words with same score
        elif word_score == max_word_score:
            # Prefer the word with the fewest letters, unless one has 10 letters
            if len(word) == 10 and len(max_word) != 10:
                max_word = word
            elif len(word) < len(max_word) and len(max_word) != 10:
                max_word = word

        max_word_score = max(max_word_score, word_score)
    return (max_word, max_word_score )
