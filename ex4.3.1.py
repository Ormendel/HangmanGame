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

def printErr(letter:str) -> None:
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

if __name__ == "__main__":
    prompt()
    letter = input("Guess a letter: ")
    printErr(letter)
    print("\nedge cases:")
    #now we check edge cases
    printErr('a') #output: a
    printErr('A') #output: a
    printErr('$') #output: E2
    printErr('ab') #output: E1
    printErr('app$') #output: E3
    printErr('app') #output: E1
    printErr('5')


    word = input("Great!, now enter a word without spaces:")
    output = ('_'+' ')*len(word)
    output = output[:-1]    #omit last space
    print(output)