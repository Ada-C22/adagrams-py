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

    final_string = []
    letters_frequency = []
    

    for letters, frequency in LETTER_POOL.items():
        for i in range(frequency):
            letters_frequency.append(letters)
    

    while len(final_string) < 10:
        letter_index = random.randint(0, len(letters_frequency) -1)

        if letters_frequency[letter_index] in final_string:
            continue
        elif letters_frequency[letter_index] not in final_string:
            final_string.append(letters_frequency[letter_index])
        
        
    return final_string


def uses_available_letters(word, letter_bank):
    available_letters = []


    for letter_item in letter_bank:
        available_letters.append(letter_item)

    for letter in word:
        uppercase_letter = letter.upper()
        if uppercase_letter in available_letters:
            
            available_letters.remove(uppercase_letter)
        else: 
            return False
    return True


def score_word(word):
    
    score_values = {
        1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
        2: ["D", "G"],
        3: ["B", "C", "M", "P"],
        4: ["F", "H", "V", "W", "Y"],
        5: ["K"],
        8: ["J", "X"],
        10: ["Q", "Z"]
    }
    score = 0
    index = 0
    word_uppercase = word.upper()
    for letter in word_uppercase:
        for num_key, letter_value in score_values.items():
            if letter in letter_value:
                score += num_key
    if  6 < len(word_uppercase) < 11:
        score += 8
    print(score)
    return score


def get_highest_word_score(word_list):
    words_entered = []
    score_data = []
    index = 0
    
    for word in word_list:
        score = score_word(word)
        score_data.append(score)
        words_entered.append(word)

    winning_score =  score_data[0]
    winning_word = words_entered[0]

    for score in score_data:
        
        if score > winning_score:
            winning_score = score_data[index]
            winning_word = words_entered[index]
        elif score == winning_score:
            if len(winning_word) == 10:
                continue
            elif len(words_entered[index]) == 10:
                winning_score = score_data[index]
                winning_word = words_entered[index]
            elif len(words_entered[index]) < len(winning_word) :
                winning_score = score_data[index]
                winning_word = words_entered[index]
            elif len(winning_word) > len(words_entered[index]):
                continue
            else:
                
                loop_count = 0
                for index_word in words_entered:
                    if index_word == winning_word:
                        winning_score_index = loop_count
                    else:
                        loop_count += 1

                if index < winning_score_index:
                    winning_score = score_data[index]
                    winning_word = words_entered[index]
                
        if index == len(score_data):
            return (winning_word, winning_score)
        else:
            
            index += 1
        
        

    return (winning_word, winning_score)








    
