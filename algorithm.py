from Merge_Sort_Algorithm import *

def main():
    input_variable = input("What are the words you want me to check? ")


    y=0
    for letters in input_variable:
        letters = letters.lower()
        if ord(letters) == 39:
            apostrophe = input_variable[y:y+2]
            input_variable = input_variable.replace(apostrophe, ' ')
        elif ord(letters) < 96:
            input_variable = input_variable.replace(input_variable[y], ' ')
            y+=1
        elif ord(letters) > 122:
            input_variable = input_variable.replace(input_variable[y], ' ')
            y+=1
        else:
            y+=1

    list = input_variable.split()

    #print()
    #print(f'This is the list of inputed words: {list}')

    suggusted_words = {

    }

    incorreect_index = []
    incorrect_word = []

    for x in list:
        x = x.lower()
        with open(f'word_list/{x[0]}.txt', 'r') as file:
            possible_words = possible_list(x)
            if search_algorithm(x) == False:
                top_4_words = suggustion(x, possible_words)
                suggusted_words[x] = top_4_words
                incorrect_word.append(x)
                incorreect_index.append(list.index(x))


    incorrect_word_index = 0
    while len(incorrect_word) > incorrect_word_index:
        current_word = incorrect_word[incorrect_word_index]
        button_1 = suggusted_words[incorrect_word[incorrect_word_index]][0]
        button_2 = suggusted_words[incorrect_word[incorrect_word_index]][1]
        button_3 = suggusted_words[incorrect_word[incorrect_word_index]][2]
        button_4 = suggusted_words[incorrect_word[incorrect_word_index]][3]
        print(f'This is the current word being printed {current_word}')
        print(button_1)
        print(button_2)
        print(button_3)
        print(button_4)
        incorrect_word_index+=1

if __name__ == "__main__":
    main()

# TODO: Establish Buttons and values for the first word
# TODO: Create a dictionary of the current incorrectly spelt word and a list of 4 possible words
# TODO: In GUI make buttons for wrongly spelled words where is you click sumbit button, changes output text box
# TODO: Use .replace to replace the inccorect word with the correct word
#TODO: Raise a numeric and a run time exception here, make sure it only takes alphabetical values

