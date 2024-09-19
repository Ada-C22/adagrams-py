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





score_chart = {'A':1, 'E':1, 'I':1, 'O': 1, 'U':1, 'L':1, 'N':1, 'R':1, 'S':1,
               'T':1, 'D':2, 'G':2, 'B':3, 'C':3, 'M':3, 'P':3, 'F':4, 'H':4,
               'V':4, 'W':4, 'Y':4, 'k':5, 'J':8, 'X':8, 'Q':10, 'Z':10}
def score_word(word):

    score_list= []
    for char in word.upper():
        if char in score_chart.keys():
            score_list.append(score_chart[char])
    total_score = sum(score_list)
    if len(word) >= 7:
        total_score = total_score + 8

    return total_score





def get_highest_word_score(word_list):
    for word in word_list:
        score = score_word(word)

