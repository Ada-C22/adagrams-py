import random 
import sys

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

SCORE_CHART = {  
    'A': 1, 
    'B': 3, 
    'C': 3, 
    'D': 2, 
    'E': 1, 
    'F': 4, 
    'G': 2, 
    'H': 4, 
    'I': 1, 
    'J': 8, 
    'K': 5, 
    'L': 1, 
    'M': 3, 
    'N': 1, 
    'O': 1, 
    'P': 3, 
    'Q': 10, 
    'R': 1, 
    'S': 1, 
    'T': 1, 
    'U': 1, 
    'V': 4, 
    'W': 4, 
    'X': 8, 
    'Y': 4, 
    'Z': 10            
}


def draw_letters():
    drawn_letters = []
    letters = list(LETTER_POOL.keys())
    used_letters = {}
    while len(drawn_letters) < 10:
        random_letter_pos = random.randint(0,25)
        random_letter = letters[random_letter_pos]
        letter_count = LETTER_POOL[random_letter]
        if random_letter in used_letters:
            used_count = used_letters[random_letter]
            if used_count < letter_count:
                drawn_letters.append(random_letter)
                used_letters[random_letter] = used_count + 1
                
        else:
            drawn_letters.append(random_letter)
            used_letters[random_letter] = 1 
    return drawn_letters


def uses_available_letters(word, letter_bank):
    letter_bank_copy = letter_bank[:]
    for letter in word:
        letter = letter.upper()
        if letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
        else:
            return False
    return True 



def score_word(word):
    score = 0 
    for letter in word:
        letter = letter.upper()
        score += SCORE_CHART[letter]
    if len(word) >=7 and len(word) < 11:
        score += 8
    return score 

def which_came_first(original_list, num, possible_winners):
    for word in original_list:
        if len(word) == num:
            for possible_winner in possible_winners:
                if word == possible_winner[0]:
                    return possible_winner 



def get_highest_word_score(word_list):
    words_and_scores = {}
    for word in word_list:
        word_score =  score_word(word)
        words_and_scores[word] = word_score
    scores = list(words_and_scores.values())
    max_score = max(scores)
    possible_winners = []
    for word, score in words_and_scores.items():
        if score == max_score:
            possible_winners.append((word, score))
    if len(possible_winners) == 1:
        return possible_winners[0]
    min = sys.maxsize # setting the min variable to a very high number 
    for possible_winner in possible_winners:
        if len(possible_winner[0]) == 10:
            return which_came_first(word_list, 10, possible_winners)
        if len(possible_winner[0]) < min:
            min = len(possible_winner[0])
    return(which_came_first(word_list, min, possible_winners))


