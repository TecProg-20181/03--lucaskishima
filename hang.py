from word import Word

def hangman():

    guesses = 8
    letters_guessed = []

    word = Word(guesses)
    secret_word = word.loadWords(guesses).lower()
    number_of_different_letters = word.countDifferentLetters(secret_word)

    print('Welcome to the game, Hangam!')
    print('I am thinking of a word that is', len(secret_word), 'letters long and have',
          number_of_different_letters, 'different letters.')
    print('-------------------------------------------------------------------')

    while  word.isWordGuessed(secret_word, letters_guessed) == False and word.guesses >0:
        print('You have ', word.guesses, 'guesses left.')

        available = word.getAvailableLetters()
        for letter in available:
            if letter in letters_guessed:
                available = available.replace(letter, '')

        print ('Available letters', available)
        letter = input('Please guess a letter: ')
        guessed = word.guessLetter(letter, secret_word, letters_guessed, guesses)

    else:
        if word.isWordGuessed(secret_word, letters_guessed) == True:
            print('Congratulations, you won!')
        else:
            print('Sorry, you ran out of guesses. The word was ', secret_word, '.')

hangman()
