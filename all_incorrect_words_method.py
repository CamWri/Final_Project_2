#All of these methods are used in all_inaccurate_words_method

def remove_incorrect_characters(input_variable:str) -> str:
    '''
    Removes all non letters and replaces them with spaces
    :param input_variable: the entire input from the user
    :return: returns the entire input from the user, but with only letters allowed
    '''
    y = 0
    for letters in input_variable:
        letters = letters.lower()
        if ord(letters) == 39:
            apostrophe = input_variable[y:y + 2]
            input_variable = input_variable.replace(apostrophe, ' ')
        elif ord(letters) < 96:
            input_variable = input_variable.replace(input_variable[y], ' ')
            y += 1
        elif ord(letters) > 122:
            input_variable = input_variable.replace(input_variable[y], ' ')
            y += 1
        else:
            y += 1
    return input_variable


def all_possible_words(input_word: str) -> list:
   '''
   Navigates through the txt file for possible words that are +/- 2 in length of the inputed word
   :param input_word:  a word from the users input
   :return: returns a list of txt file words length that are +/- 2 of the inputed word's length
   '''
   with open(f'word_list/{input_word[0]}.txt', 'r') as file:
       possible_words = []
       for line in file:
           if len(line) < len(input_word) + 2 and len(input_word) - 2 < len(line):
               possible_words.append(line[0:].rstrip('\n'))
   return possible_words

def word_exists(input_word: str) -> bool:
   '''
   Checks to see if the input_word exists in the .txt files
   :param input_word:  a word from the users input
   :return: A boolean to see if the work exists in our database or not
   '''
   list = all_possible_words(input_word)
   y = 0
   for y in list:
       if y == input_word:
           return True
   else:
       return False

