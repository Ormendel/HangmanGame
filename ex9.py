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

def choose_word(file_path, index):
    COMMA = ' '
    wordsFile = open(file_path, "r")
    row = wordsFile.readline()
    wordsFile.close() #there is only one line in the file, so we can close it now
    tempList = row.split(COMMA)

    index %= len(tempList)
    # now search for the specific index
    outputStr = tempList[index-1] # because the index is starting from 1 and not zero
    return len(set(tempList)), outputStr


if __name__ == "__main__":
    prompt()
    wordsFile = open("words.txt", "w")
    wordsFile.write("Strawberry Banana Apple Strawberry Banana Pineapple Mango Melon Strawberry Banana Pineapple Mango Melon Apple")
    wordsFile.close()
    # finished writing
    myTuple = choose_word("words.txt",16)
    print(myTuple)

    wordsFile = open("words2.txt", "w")
    wordsFile.write("hangman song most broadly is a song hangman work music work broadly is typically")
    wordsFile.close()
    myTuple = choose_word("words2.txt", 15)
    print(myTuple)






