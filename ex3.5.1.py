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

letter = input("Guess a letter: ")
print(letter.lower())

word = input("Great!, now enter a word without spaces:")
output = ('_'+' ')*len(word)
output = output[:-1]    #omit last space
print(output)