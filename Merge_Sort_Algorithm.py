from four_sugguested_words_method import *
from all_incorrect_words_method import *

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


