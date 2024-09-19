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

    my_list = [] #creating an empty list to collect randomly picked letter

    #converting dictionary keys into list representing the 'count' times of letter and storing in pool_list
    pool_list = []
    for letter, count in LETTER_POOL.items():
        pool_list += [letter] * count # add letter 'count' times to pool_list
        
    while len(my_list) < 10:
        random_key = random.randint(0, len(pool_list) - 1) #randomly select index from pool_list
        
        random_letter = pool_list[random_key] #getting letter associated with index
        pool_list.remove(random_letter) #removing letter from pool_list
        my_list.append(random_letter) #adding this letter to my_list

    return my_list


letter_bank = draw_letters() # retreiving my_list of 10 listter from draw_letter function

word = "SANTAAA"


def uses_available_letters(word, letter_bank):

    # getting user input as string 
    upper_word = word.upper()

    letter_bank_dict = {} #empty dictionary to store 
    inputed_word_dict = {} #empty dictionary to store letter and frequency from user


    # adding upper_word into inputed_word_dict with letter: count format
    for letter in upper_word:
        if letter not in inputed_word_dict:
            inputed_word_dict[letter] = 1 #Initialize with one if letter added first time
        else:
            inputed_word_dict[letter] += 1 #Increment by 1 if letter added additionally
    

    # converting answer_list to a letter_bank_dict with a format of letter:count
    for letter in letter_bank:
        if letter not in letter_bank_dict:
            letter_bank_dict[letter] = 1
        else:
            letter_bank_dict[letter] += 1


    # comparing letter_bank_dict and inputed_word_dict 
    for key, value in inputed_word_dict.items():
        if key not in letter_bank_dict or value > letter_bank_dict[key]:  # checking if key from inputed_word_dict is in letter_bank_dict and checking if value of inputed_word_dict is greater than value in letter_bank_dict
            return False
        
    return True


x = uses_available_letters(word, letter_bank)


def score_word(word):
    score_dict = {
        'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1,
        'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
        'D': 2, 'G': 2,
        'B': 3, 'C': 3, 'M': 3, 'P': 3,
        'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
        'K': 5,
        'J': 8, 'X': 8,
        'Q': 10, 'Z': 10
    }
    #getting user input as string 
    upper_word = word.upper()
    score = 0

    # incrementing score with values from score_dict
    for letter in upper_word:
        if letter in score_dict:
            score += score_dict[letter]
    # If the length of the word is 7, 8, 9, or 10: score gets incremented by 8
    if len(upper_word) in (7,8,9,10):
        score += 8
    
    return score




def get_highest_word_score(word_list):
    
    winning_score = 0
    winning_word = None
    word_score_dict = {}
    first_ten_letter_word = None

    # iterate over word_list to create score_list
    for word in word_list:
        running_score = score_word(word) # calculating score of word with score_word function
        word_score_dict[word] = running_score

    #keep track of first 10 letter word:
        if len(word) == 10 and first_ten_letter_word is None:
            first_ten_letter_word = word
        
    # iterating through dictionary
    for word, score in word_score_dict.items():
        if score > winning_score:
            winning_score = score
            winning_word = word

        # Tie breaker
        elif score == winning_score: #if score is same shorter length word wins

            if len(word) == 10: #length is shorter and 
                if word == first_ten_letter_word:
                    winning_score = score
                    winning_word = word
            
            
            elif len(word) < len(winning_word) and len(winning_word) != 10: #shorten length word wins!
                winning_score = score
                winning_word = word

            
    return (winning_word, winning_score)



