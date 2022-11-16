from Merge_Sort_Algorithm import *

def main():
    input_variable = input("What are the words you want me to check? ")


    y=0
    #TODO: Raise a numeric exception here, make sure it only takes alphabetical values
    for letters in input_variable:
        letters = letters.lower()
        #TODO: look in depth with the ascii values to specigy if you remove or remove and add a space.
        if ord(letters) < 96:
            input_variable = input_variable.replace(input_variable[y], ' ')
            y+=1
        elif ord(letters) > 122:
            input_variable = input_variable.replace(input_variable[y], ' ')
            y+=1
        else:
            y+=1


    print(input_variable)

    list = input_variable.split()

    print()
    print(f'This is the list of inputed words: {list}')

    for x in list:
        print()
        x = x.lower()
        with open(f'word_list/{x[0]}.txt', 'r') as file:

            print(f'This is the word I am working on: {x}')

            possible_words = possible_list(x)

            if search_algorithm(x) == True:
                numeric_list = []
                for letters in x:
                    numbers = ord(letters) - 96
                    numeric_list.append(numbers)
                print('This Value Exists')
                print(f'This is the list of possible words: \n{possible_words}')
                print(f'The Numeric List is: {numeric_list}')
            else:
                print('This Word does not exists in the current dictionary')
                # TODO: If a word does not currently exist in the files, add a button to maually allow the word to be added into the file
                # TODO: Add algrorith for word suggestions by using a list full of dictionaries or a dictionary filled with 2list, word and the value
            print()

if __name__ == "__main__":
    main()


#TODO: Add more words, specifically concationation
