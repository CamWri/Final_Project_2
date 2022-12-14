#All of these methods are used in all_inaccurate_words_method

def remove_incorrect_characters(input_variable:str) -> str:
    '''
    Raises exceptions for non-letters except apostrophes and spaces
    :param input_variable: the entire input from the user
    :return: returns the entire input from the user, but with only letters allowed
    '''
    incorrect_characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',', '-', '\"', '.', '!', '?', '/', '(', ')', '[', ']', '#', '&']
    for characters in input_variable:
        if characters in incorrect_characters:
            input_variable = ''
            raise ValueError
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

