def search_algorithm(input_word):
    list = possible_list(input_word)
    input_letters = []
    list_all_letters = []
    for letters in input_word:
        input_letters.append(letters)

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


def suggustion_list(input_word):
    with open(f'word_list/{input_word[0]}.txt', 'r') as file:
        suggusted_words = []
        for line in file:
            for letters in line:
                pass
