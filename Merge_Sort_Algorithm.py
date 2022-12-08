<<<<<<< Updated upstream
def search_algorithm(input_word):
    list = possible_list(input_word)
=======
from four_sugguested_words_method import *
from all_incorrect_words_method import *
>>>>>>> Stashed changes

def all_incorrect_words(input_variable: str) -> list:
    '''
    Iterates to append incorrect words, indexes, and suggusted words to be used later on
    :param input_variable: the entire input from the user
    :return: a list with a dictionary of the word and its four suggusted values, the incorrect words index, and the incorrect word
    '''
    input_variable = remove_incorrect_characters(input_variable)

    list = input_variable.split()

    suggusted_words = {

    }

    incorreect_index = []
    incorrect_word = []

    for x in list:
        with open(f'word_list/{x.lower()[0]}.txt', 'r') as file:
            possible_words = all_possible_words(x.lower())
            if word_exists(x.lower()) == False:
                top_4_words = four_suggested_words(x, possible_words)
                suggusted_words[x] = top_4_words
                incorrect_word.append(x)
                incorreect_index.append(list.index(x))

    return [suggusted_words, incorreect_index, incorrect_word]


def four_suggested_words(word: str, list_of_possible_words: list) -> list:
    '''
    Establish what four words are being suggusted for the incorrect word
    :param word:  a word from the users input
    :param list_of_possible_words: all the possible words after from a txt file where the files words length is +/- 2 of an
    inputed word
    :return: a list of four words that are sugguested if the inputed word is wrong
    '''
    possible_words = list_of_possible_words
    x = word
    all_suggusted_word = {

    }

    top_4_words = []
    correction = 0

    max_coorelation = coorelation_to_input(all_suggusted_word, possible_words, x)

    repetition = True
    while repetition:
       similar_words = []
       #Establish what words equal the correlation value
       for word_list in all_suggusted_word:
           if all_suggusted_word[word_list] == max_coorelation - correction:
               similar_words.append(word_list)

       repetition = algorithm_for_suggustions(repetition, similar_words, top_4_words, x)

       correction+=1
    return top_4_words


<<<<<<< Updated upstream
def suggustion(word, list_of_possible_words):
    possible_words = list_of_possible_words
    x = word
    all_suggusted_word = {

    }

    top_4_words = []

    first_iteration = []

    for y in possible_words:
        if len(y) < len(x) + 2 and len(x) - 2 < len(y):
            first_iteration.append(y)

    for current_word_ in first_iteration:
        total_letters = []
        for letters in current_word_:
            all_suggusted_word[current_word_] = all_suggusted_word.get(current_word_, 0)
            if letters not in total_letters:
                if letters in x:
                    all_suggusted_word[current_word_] = all_suggusted_word.get(current_word_) + 1
                    total_letters.append(letters)
    max_coorelation = max(all_suggusted_word.values())

    correction = 0
    repetition = True
    while repetition:
        similar_words = []
        for word_list in all_suggusted_word:
            if all_suggusted_word[word_list] == max_coorelation - correction:
                similar_words.append(word_list)
        for words_in_similar in similar_words:
            if len(top_4_words) < 4:
                if words_in_similar[:2] == x[:2]:
                    top_4_words.append(words_in_similar)
                elif len(words_in_similar) == len(x):
                    top_4_words.append(words_in_similar)
            else:
                repetition = False
                break

        correction+=1
    return top_4_words


def analyze(input_variable):
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

    list = input_variable.split()

    # print()
    # print(f'This is the list of inputed words: {list}')

    suggusted_words = {

    }

    incorreect_index = []
    incorrect_word = []

    for x in list:
        with open(f'word_list/{x.lower()[0]}.txt', 'r') as file:
            possible_words = possible_list(x.lower())
            if search_algorithm(x.lower()) == False:
                top_4_words = suggustion(x, possible_words)
                suggusted_words[x] = top_4_words
                incorrect_word.append(x)
                incorreect_index.append(list.index(x))
    return [suggusted_words, incorreect_index, incorrect_word]
=======
>>>>>>> Stashed changes
