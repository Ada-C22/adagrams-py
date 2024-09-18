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
POINTS_FOR_LETTER = {'A': 1,
                    'E': 1,
                    'I': 1,
                    'O': 1, 
                    'U': 1,
                    'L': 1,
                    'N': 1,
                    'R': 1, 
                    'S': 1,
                    'T': 1,
                    'D': 2,
                    'G': 2,
                    'B': 3,
                    'C': 3,
                    'M': 3,
                    'P': 3,
                    'F': 4,
                    'H': 4,
                    'V': 4,
                    'W': 4,
                    'Y': 4,
                    'K': 5,
                    'J': 8,
                    'X': 8,
                    'Q': 10,
                    'Z': 10}
def draw_letters():
    letter_pool = []
    list = []
    hand_bank = []

    for letter_qunt in LETTER_POOL.items():
        list.append(letter_qunt)

    for letter_qunt in list:
        letter = letter_qunt[0]
        qunt = int(letter_qunt[1])
        while qunt > 0:
            letter_pool.append(letter)
            qunt = qunt - 1
    for idx in range(0, 10):
            idx = random.randint(0, len(letter_pool)-1)
            hand_bank.append(letter_pool[idx])
            del letter_pool[idx]
    return hand_bank



def uses_available_letters(word, letter_bank):
    letter_bank = letter_bank.copy()
    for letter in word:
        letter = letter.upper()
        if letter not in letter_bank:
            return False
        letter_bank.remove(letter)
    return True



def score_word(word):
    word = word.upper()
    points = 0
    for letter in word:
        points += POINTS_FOR_LETTER[letter]
    if 6 < len(word) < 11:
        points +=8
    return points           


def get_highest_word_score(word_list):
    score_max = 0
    word_min = "ZZZZZZZZZZZZZZZZZ"
    words_list_pos_win = []

    for word in word_list:
        words_score = (score_word(word))

        if words_score > score_max:
            score_max = words_score

    for word in word_list:
        words_score = (score_word(word))
        if score_max == words_score:
            words_list_pos_win.append(word)
    if len(words_list_pos_win) == 1:
        return(words_list_pos_win[0], score_max)
    for word in words_list_pos_win:
        if len(word) == 10:
            return(word, score_max)
        if len(word) < len(word_min):
            word_min = word
    return(word_min, score_max)

        
    

