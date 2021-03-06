import random


def loadWord():
   f = open('words.txt', 'r')
   wordsList = f.readlines()
   f.close()

   wordsList = wordsList[0].split(' ')
   secretWord = random.choice(wordsList)
   return secretWord


def isWordGuessed(secretWord, lettersGuessed):
    """
    See if user guessed the word.

    secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: boolean, True only if all the letters of secretWord are in lettersGuessed;
      False otherwise
    """
    # FILL IN YOUR CODE HERE...
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    """
    Return the guessed word so far.

    secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: string, of letters and underscores.  For letters in the word that the user has
    guessed correctly, the string should contain the letter at the correct position.  For letters
    in the word that the user has not yet guessed, shown an _ (underscore) instead.
    """
    # FILL IN YOUR CODE HERE...
    returnedWordArr = []
    returnedWord = ""
    secretWordArr = list(secretWord)
    # Replace SecretWord with '_'.
    for letter in secretWord:
        returnedWordArr.append("_")
    # Replace '_' with correctly guessed letters
    for letter in lettersGuessed:
        if letter in secretWordArr:
            if secretWord.count(letter) == 1:
                returnedWordArr[secretWord.index(letter)] = letter
            else:
                indices = [i for i, x in enumerate(secretWordArr) if x == letter]
                for index in indices:
                    returnedWordArr[index] = letter
    return returnedWord.join(returnedWordArr)



def hangman(secretWord):
    """
    secretWord: string, the secret word to guess.

    Starts up a game of Hangman in the command line.
    * At the start of the game, let the user know how many
      letters the secretWord contains.
    * Ask the user to guess one letter per round.
    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.
    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
    """
    # FILL IN YOUR CODE HERE...
    lettersGuessed = []
    guessesLeft = 7
    print("Welcome to Hangman! Can You Guess the Secret Word?")
    # How many letters are there left to guess?
    while guessesLeft > 0 and not isWordGuessed(secretWord, lettersGuessed):
        lettersLeft = str((getGuessedWord(secretWord, lettersGuessed).count("_")))
        print("Secret Word Progress (There are " + str(lettersLeft) + " letters left): " + getGuessedWord(secretWord, lettersGuessed))
        # Get User Letter Guess
        userLetterGuess = ''
        while not userLetterGuess.isalpha():
            userLetterGuess = raw_input("Guess a letter ('?' to see letters already guessed): ")
            if(len(userLetterGuess) > 1):
                userLetterGuess = ''
            elif(userLetterGuess in lettersGuessed):
                print("You guessed that letter already")
                userLetterGuess = ''
            elif(userLetterGuess == "?"):
                print("".join(lettersGuessed))
        # Add UserGuess to LettersGuessed
        lettersGuessed.append(userLetterGuess)
        if userLetterGuess in secretWord:
            print("Yes! '" + userLetterGuess + "' is in the Secret Word!")
            if isWordGuessed(secretWord, lettersGuessed):
                print("You guessed the Word " + secretWord + "! Congrats!")
        else:
            guessesLeft -= 1
            if guessesLeft > 0:
                print("Nope! Guess Again! You have " + str(guessesLeft) + " guesses left.")
            else:
                print("You Failed! The word was " + secretWord + "...")


secretWord = loadWord()
hangman(loadWord())
