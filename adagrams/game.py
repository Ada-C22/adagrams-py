

def draw_letters():
    # array_of_strings = [ ]
    player = []
    for letters in draw_letters():
        player = [draw_letters(letters)]
    return player

# def uses_available_letters(word, letter_bank):
    word = word.upper()
    letter_bank_remaining = letter_bank.copy()

    for letter in word:
        if letter in letter_bank_remaining:
            letter_bank_remaining.remove(letter)
        else:
            return False
    return True
    

# def score_word(word):
#     pass

# def get_highest_word_score(word_list):
#     pass