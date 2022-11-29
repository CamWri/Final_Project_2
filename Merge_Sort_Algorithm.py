def search_algorithm(input_word):
    list = possible_list(input_word)
    input_letters = []
    #for letters in input_word:
        #input_letters.append(letters)

    y = 0
    for y in list:
        if y == input_word:
            return True
    else:
        return False



def possible_list(input_word):
    with open(f'word_list/{input_word[0]}.txt', 'r') as file:
        possible_words = []
        for line in file:
            possible_words.append(line[0:].rstrip('\n'))

    return possible_words


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
