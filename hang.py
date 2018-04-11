from word import Word

def hangman():

    guesses = 8
    lettersGuessed = []

    word = Word(guesses)
    secretWord = word.loadWords().lower()

    print('Welcome to the game, Hangam!')
    print('I am thinking of a word that is', len(secretWord), ' letters long.')
    print('-------------')

    while  word.isWordGuessed(secretWord, lettersGuessed) == False and word.guesses >0:
        print('You have ', word.guesses, 'guesses left.')

        available = word.getAvailableLetters()
        for letter in available:
            if letter in lettersGuessed:
                available = available.replace(letter, '')

        print ('Available letters', available)
        letter = input('Please guess a letter: ')
        guessed = word.guessLetter(letter, secretWord, lettersGuessed, guesses)

    else:
        if word.isWordGuessed(secretWord, lettersGuessed) == True:
            print('Congratulations, you won!')
        else:
            print('Sorry, you ran out of guesses. The word was ', secretWord, '.')

hangman()
