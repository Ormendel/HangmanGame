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


def printErr(letter: str) -> None:
    """
    This function prints error depends on size of letter and alphabetical order
    :param letter: string which we get from user
    :return: None
    """
    size_above1 = len(letter) > 1
    only_abcletters = letter.isalpha()
    if not (size_above1) and only_abcletters:
        print(letter.lower())
    elif size_above1 and not (only_abcletters):
        print("E3")
    elif only_abcletters == False:
        print("E2")
    elif size_above1:
        print("E1")


def is_valid_input(letter_guessed):
    size_above1 = len(letter_guessed) > 1
    only_abcletters = letter_guessed.isalpha()
    if (not size_above1) and only_abcletters:
        return True
    elif size_above1 and not only_abcletters:
        return False
    elif only_abcletters == False:
        return False
    elif size_above1:
        return False


def check_valid_input(letter_guessed, old_letters_guessed):
    """

    :param letter_guessed: what character(s) did the user guess
    :param old_letters_guessed: list of all guessed characters
    :return: Boolean value
    """

    if not is_valid_input(letter_guessed):
        return False
    elif letter_guessed.lower() in old_letters_guessed:  # if we reached here, it's assured letter_guesses is one alphabetical letter
        return False
    return True


def show_hidden_word(secret_word="mammals", old_letters_guessed=['s', 'p', 'j', 'i', 'm', 'k']):
    outputList = list(secret_word) # transform to list because we need to change this string
    for letter in outputList:
        if not (letter in old_letters_guessed):
            for index in range(len(secret_word)):
                if outputList[index] == letter:
                    outputList[index] = '_'
        else:
            continue

    # now transform outputList back to a string
    outputStr = ""
    size = len(outputList)
    for i in range(size):
        if i == size - 1:
            outputStr += outputList[i]
        else:
            outputStr += outputList[i] + ' '
    return outputStr


if __name__ == "__main__":
    prompt()

    secret_word = "mammals"
    old_letters_guessed = ['s', 'p', 'j', 'i', 'm', 'k']
    print(show_hidden_word(secret_word, old_letters_guessed))
    print(show_hidden_word("abba", ['p','q','i'])) # output: _ _ _ _
