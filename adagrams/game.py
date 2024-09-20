import random
def draw_letters():
   letter_pool = {
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
# using random.choice
#    while len(drawn_letters) < 10:

#     #extracting all the keys from dictionary
#     letter_pool_keys = letter_pool.keys()
#     letter = random.choice(list(letter_pool_keys))
#     if letter_pool[letter] > 0:
#         drawn_letters.append(letter)

#         #adding random letter to the list and decreasing the frequency of the letter
#         letter_pool[letter]-= 1
#    return drawn_letter


   total_letters = sum(letter_pool.values())

   while len(drawn_letters) < 10:
        # Generating a random number between 1 and the total number of letters
        rand_num = random.randint(1, total_letters)

        # Finding  the corresponding letter
        cumulative_count = 0
        for letter, frequency in letter_pool.items():
            cumulative_count += frequency
            if rand_num <= cumulative_count:
                drawn_letters.append(letter)
                letter_pool[letter] -= 1
                total_letters -= 1
                break


   return drawn_letters


def uses_available_letters(word, letter_bank):

#    converting all the letters in letter bank to upper case
    letter_bank = [letter.upper() for letter in letter_bank]
# making a dictionary for a letter_bank to check the frequency of letters
    lookup = {}
    for letter in letter_bank:
        if letter in lookup:
            lookup[letter] += 1
        else:
            lookup[letter] = 1
    #converting all the letters of word into uppercase and checking the frequebcy of the letter, if found decrementing the value or else returning false

    for letter in word.upper():
        if letter not in lookup or lookup[letter] == 0:
            return False
        else:
            lookup[letter] -= 1
    return True

#Approaching as per draw_letters function with nested loops

# def score_word(word):
# #    converting all the letters in letter bank to upper case
#     word = [letter.upper() for letter in word]
#     total_score = 0
#     # making a dictionary with letters and it's score value
#     score_value = {
#         'AEIOULNRST': 1,'DG': 2, 'BCMP': 3, 'FHVWY': 4, 'K': 5, 'JX': 8, 'QZ': 10
#         }

#     for letter in word:
#         for scoring_letter_group, score in score_value.items():
#             if letter in scoring_letter_group:
#                 total_score+= score
#     if len(word) > 6 and len(word) <=10:
#         total_score += 8
#     return total_score



# optimal solution where dictionary is created for individual letter and score value without nested loops
def score_word(word):
    score_value = {
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

    total_score+= sum(score_value.get(letter, 0) for letter in word )

    if len(word) > 6 and len(word) <=10:
        total_score += 8

    return total_score



def get_highest_word_score(word_list):
    max_word = word_list[0]
    max_word_score =score_word(max_word)
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
    return (max_word,max_word_score )
