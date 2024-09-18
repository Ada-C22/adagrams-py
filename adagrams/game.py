import random

def draw_letters():
    hand = []
    letters_list = []
    LETTER_POOL = {
    'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3,
    'H': 2, 'I': 9, 'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6,
    'O': 8, 'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6, 'U': 4,
    'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1
    }

    #make dictionary into a list 
    for letter, count in LETTER_POOL.items():
        letters_list.extend(letter * count)

    #make a hand of 10 letters 
    
    letters = []
    temporary_letters_list = letters_list.copy()
    for letter in range(0,10):
        
        random_number = random.randint(0,len(temporary_letters_list)-1)

        #remove the letter from list 
        random_letter = temporary_letters_list.pop(random_number)
        letters.append(random_letter)
    
    return letters 

def uses_available_letters(word, letter_bank):
    word = word.upper()
    temporary_letter_bank = letter_bank[:]
    for letter in word: 
        if letter not in temporary_letter_bank:  
            return False
        temporary_letter_bank.remove(letter) 
    return True

def score_word(word):

    score_one_point = ["A","E","I","O","U","L","N","S","T"]
    score_two_point =["D","G"]
    score_three_point = ["B","C","M","P"]
    score_four_point = ["F","H","V","W","Y"]
    score_five_point = ["K"]
    score_eight_point = ["J","X"]
    score_ten_point = ["Q","Z"]

    score = 0

    word = word.upper()
            
    if len(word) >= 7:
        score += 8

    for letter in word: 
        if letter in score_one_point:
            score  += 1
        elif letter in score_two_point:
            score += 2
        elif letter in score_three_point:
            score += 3
        elif letter in score_four_point:
            score += 4
        elif letter in score_five_point:
            score += 5
        elif letter in score_eight_point:
            score += 8
        elif letter in score_ten_point: 
            score += 10 


    return score
        
        

def get_highest_word_score(word_list):

    score_list = []
    for word in word_list:

        score_for_word = score_word(word)
        score_list.append(score_for_word)

    score_word_tuple = tuple(zip(word_list,score_list))

    best_word = score_word_tuple[0]

    for i in range(1, len(score_word_tuple)):
        
        if best_word[1] < score_word_tuple[i][1]:
            best_word = score_word_tuple[i]

        elif best_word[1] == score_word_tuple[i][1]:
            length_best_word = len(best_word[0])
            length_next_word = len(score_word_tuple[i][0])
            if length_best_word != 10:
                if length_next_word == 10:
                    best_word = score_word_tuple[i]
                if length_next_word <= length_best_word:
                    best_word = score_word_tuple[i]

    return best_word

                 


#create a bank for word scores called score_list
#run through each number in the list and determine largest value 
#create a tuple where index zero is the word and index 1 is the score
#if there are 2 words with the same score then choose shorter word 
        
        #index 0 string, index 1 score of word 
   



 

def test_letter_not_selected_too_many_times():
    pass    
