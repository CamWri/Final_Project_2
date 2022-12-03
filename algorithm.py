from Merge_Sort_Algorithm import *

def main():
    input_variable = input("What are the words you want me to check? ")

    analyzed = analyze(input_variable)

    suggusted_words = analyzed[0]
    incorreect_index = analyzed[1]
    incorrect_word = analyzed[2]


    print(f'This is the variable analyzed:{analyzed}')
    print(f'This is the variable incorreect_index:{incorreect_index}')
    print(f'This is the variable incorrect_word:{incorrect_word}')





    incorrect_word_index = 0
    while len(incorrect_word) > incorrect_word_index:
        current_word = incorrect_word[incorrect_word_index]
        button_1 = suggusted_words[incorrect_word[incorrect_word_index]][0]
        button_2 = suggusted_words[incorrect_word[incorrect_word_index]][1]
        button_3 = suggusted_words[incorrect_word[incorrect_word_index]][2]
        button_4 = suggusted_words[incorrect_word[incorrect_word_index]][3]
        print(f'This is the current word being printed {current_word}')
        print(f'Button 1 - {button_1}')
        print(f'Button 2 - {button_2}')
        print(f'Button 3 - {button_3}')
        print(f'Button 4 - {button_4}')
        incorrect_word_index+=1

if __name__ == "__main__":
    main()

# TODO: Establish Buttons and values for the first word
# TODO: Create a dictionary of the current incorrectly spelt word and a list of 4 possible words
# TODO: In GUI make buttons for wrongly spelled words where is you click sumbit button, changes output text box
# TODO: Use .replace to replace the inccorect word with the correct word
#TODO: Raise a numeric and a run time exception here, make sure it only takes alphabetical values
#TODO: GO through word files and lower all of them
