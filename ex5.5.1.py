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
    HANGMAN_ASCII_ART = 'Welcome to the game Hangman' + SEPERATOR+DRAW+str(MAX_TRIES)
    print(HANGMAN_ASCII_ART)

def is_valid_input(letter_guessed):
    size_above1 = len(letter_guessed) > 1
    only_abcletters = letter_guessed.isalpha()
    if not size_above1 and only_abcletters:
        return True
    elif size_above1 and not (only_abcletters):
        return False
    elif only_abcletters == False:
        return False
    elif size_above1:
        return False

if __name__ == "__main__":
    prompt()
    letter = input("Guess a letter: ")
    print(is_valid_input(letter))
    print("\nedge cases:")
    #now we check edge cases
    print(is_valid_input('a')) #output: True
    print(is_valid_input('A')) #output: True
    print(is_valid_input('$')) #output: False
    print(is_valid_input('ab')) #output: False
    print(is_valid_input('app$')) #output: False

    # word = input("Great!, now enter a word without spaces:")
    # output = ('_'+' ')*len(word)
    # output = output[:-1]    #omit last space
    # print(output)