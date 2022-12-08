#All of these methods are used in four_suggusted_words_method

def coorelation_to_input(all_suggusted_word: dict, possible_words: str, x: str) -> int:
    '''
    Establishes each correlation value in realtion the the amount of similar letters for the input word and the word in the txt file, gets the biggest value
    :param all_suggusted_word: a dictionary of all the suggusted words with the appropriate word
    :param possible_words: a list of all possible words for the current incorrectly inputed word
    :param x: a word from the users input
    :return: the biggest correlation value
    '''
    for current_word_ in possible_words:
        total_letters = []
        for letters in current_word_:
            all_suggusted_word[current_word_] = all_suggusted_word.get(current_word_, 0)
            if letters not in total_letters:
                if letters in x:
                    all_suggusted_word[current_word_] = all_suggusted_word.get(current_word_) + 1
                    total_letters.append(letters)
    max_coorelation = max(all_suggusted_word.values())
    return max_coorelation

def algorithm_for_suggustions(repetition: bool, similar_words: list, top_4_words: list, x: str) -> bool:
    '''
    The way to establish what words to suggust until four words are suggusted
    :param repetition: boolean value to see if there are 4 values for suggustioning
    :param similar_words: list of words in realtion to its correlaton
    :param top_4_words: the top four suggusted words
    :param x:  a word from the users input
    :return: A boolean value to see if there are four words for suggusting
    '''
    for words_in_similar in similar_words:
        if len(top_4_words) < 4:
            if words_in_similar[:3] == x[:3]:
                top_4_words.append(words_in_similar)
            elif len(words_in_similar) == len(x):
                top_4_words.append(words_in_similar)
            elif len(words_in_similar) == len(x) - 1:
                top_4_words.append(words_in_similar)
        else:
            repetition = False
    return repetition
