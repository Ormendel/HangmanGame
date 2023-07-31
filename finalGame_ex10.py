''' global variables '''
MAX_TRIES = 6
num_of_tries = 0
old_letters_guessed = []
secretWord = "change me after getting input"
revealLetters = "change me also after getting input"
''' global variables '''


def prompt() -> None:
    """
    This function outputs prompt of Hangman game to the user
    :return: None
    """
    LINE1 = "  _    _  "
    LINE2 = " | |  | |  "
    LINE3 = " | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  "
    LINE4 = " |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ "
    LINE5 = " | |  | | (_| | | | | (_| | | | | | | (_| | | | |"
    LINE6 = " |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|"
    LINE7 = "                      __/ |                      "
    LINE8 = "                     |___/"
    SEPERATOR = "\n"
    DRAW = LINE1 + SEPERATOR + LINE2 + SEPERATOR + LINE3 + SEPERATOR + LINE4 + SEPERATOR + LINE5 + SEPERATOR + LINE6 + SEPERATOR + LINE7 + SEPERATOR + LINE8 + SEPERATOR
    MAX_TRIES = 6
    HANGMAN_ASCII_ART = 'Welcome to the game Hangman' + SEPERATOR + DRAW + str(MAX_TRIES)
    print(HANGMAN_ASCII_ART)


def check_win(secret_word, old_letters_guessed):
    return revealLetters.replace(' ','') == secret_word


def show_hidden_word(secret_word, old_letters_guessed):
    outputList = list(secret_word)  # transform to list because we need to change this string
    for letter in outputList:
        if not (letter in old_letters_guessed):
            for index in range(len(secret_word)):
                if outputList[index] == letter:
                    outputList[index] = '_'
        else:
            continue

    # now transform outputList back to a string
    outputStr = ' '.join(list(outputList))
    return outputStr


def is_valid_input(letter_guessed):
    size_above1 = len(letter_guessed) > 1
    only_abcletters = letter_guessed.isalpha() and is_all_letters(letter_guessed)
    if (not size_above1) and only_abcletters:
        return True
    elif size_above1 and not only_abcletters:
        return False
    elif not only_abcletters:
        return False
    elif size_above1:
        return False


def check_valid_input(letter_guessed, old_letters_guessed):
    """

    :param letter_guessed: what character(s) did the user guess
    :param old_letters_guessed: list of all guessed characters
    :return: Boolean value - true if it's not in old_letters_values and false otherwise
    """

    if not is_valid_input(letter_guessed):
        return False
    elif letter_guessed.lower() in old_letters_guessed:  # if we reached here, it's assured letter_guesses is one alphabetical letter
        return False

    return True


def print_hangman(num_of_tries):
    HANGMAN_PHOTOS = {0: """
        x-------x""",
                      1: """
            x-------x
            |
            |
            |
            |
            |
""", 2: """
                    x-------x
                    |       |
                    |       0
                    |
                    |
                    |
        """, 3: """
                        x-------x
                        |       |
                        |       0
                        |       |
                        |
                        |
            """, 4: """
                            x-------x
                            |       |
                            |       0
                            |      /|\\
                            |
                            |
                """, 5: """
                            x-------x
                            |       |
                            |       0
                            |      /|\\
                            |      /
                            |
                """, 6: """
                            x-------x
                            |       |
                            |       0
                            |      /|\\
                            |      / \\
                            |
                """}

    print(HANGMAN_PHOTOS[num_of_tries])


def choose_word(file_path, index):
    COMMA = ' '
    wordsFile = open(file_path, "r")
    row = wordsFile.readline()
    wordsFile.close()  # there is only one line in the file, so we can close it now
    tempList = row.split(COMMA)

    index %= len(tempList)
    # now search for the specific index
    outputStr = tempList[index - 1]  # because the index is starting from 1 and not zero
    return len(set(tempList)), outputStr


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed, old_letters_guessed):
        if letter_guessed not in old_letters_guessed:
            old_letters_guessed.append(letter_guessed)
            globals()["old_letters_guessed"] = old_letters_guessed
        else:
            print('X')
            if len(old_letters_guessed) > 0:
                print(' -> '.join(old_letters_guessed))
                return False

        if letter_guessed not in secretWord:
            globals()["num_of_tries"] += 1
            print(":(")
            print_hangman(num_of_tries)
            print(globals()["revealLetters"])
            return False
        else:
            globals()["revealLetters"] = show_hidden_word(secretWord, old_letters_guessed)
            print(globals()["revealLetters"])
            return True
    print('X')
    if len(old_letters_guessed) > 0:
        print(' -> '.join(old_letters_guessed))
    return False

import re

def is_all_letters(input_string):
    return bool(re.fullmatch(r'[a-zA-Z]+', input_string))

if __name__ == "__main__":
    '''
    INTRO AND INITIALIZATION TO GLOBAL VARIABLES
    '''
    prompt()
    print("\nBEGIN! \n")
    wordsFile = open("input.txt", "w")
    wordsFile.write(
        "cat aviva or chen tom tal noy stav ofek shahar dad mom adi stav tal liat amit shiri tomer hangman noa yuval topaz ori idan ofir gili meitar adir gaya yarden sarit liri mia yanai ronit shamir")
    wordsFile.close()

    file_path = input("Enter file path: ")  # please copy this: C:\Users\ormen\PycharmProjects\selfPY_campusIL\input.txt
    index = int(input("Enter index: "))  # please enter the number 19 (position of 'Hangman')
    print("\nLet's start!\n")
    print_hangman(num_of_tries)
    globals()["secretWord"] = choose_word(file_path, index)[1].lower() # extract the secret word
    globals()["revealLetters"] = ""
    for i in range(len(secretWord)-1):
        revealLetters += '_ '
    revealLetters += '_'

    print(revealLetters)

    '''
    Now to the game!
    '''
    while num_of_tries < MAX_TRIES:
        letterGuess = input("Guess a letter: ")
        flag = try_update_letter_guessed(letterGuess.lower(), old_letters_guessed)

        if flag and check_win(secretWord, old_letters_guessed):
            print("WIN")
            break

    if num_of_tries == MAX_TRIES:
        print("LOSE")
