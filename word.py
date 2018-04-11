import random
import string

WORDLIST_FILENAME = "words.txt"


class Word():

    def __init__(self, guesses):
        self.letters_guessed = []
        self.guesses = guesses

    def loadWords(self, guesses):
        """
        Depending on the size of the word list, this function may
        take a while to finish.
        """
        print("Loading word list from file...")

        # opening and reading file.
        with open(WORDLIST_FILENAME) as inFile:
            read_data = inFile.read()

        # wordlist: list of strings
        wordlist = str.split(read_data)

        print ("  ", len(wordlist), "words loaded.")
        word = random.choice(wordlist)

        while len(word) > guesses:
            word = random.choice(wordlist)

        return word

    def guessLetter(self, letter, secret_word, letters_guessed, guesses):
        if letter in letters_guessed:

            guessed = self.guessedLetters(secret_word, letters_guessed)

            print('Oops! You have already guessed that letter: ', guessed)
        elif letter in secret_word:
            letters_guessed.append(letter)

            guessed = self.guessedLetters(secret_word, letters_guessed)

            print('Good Guess: ', guessed)
        else:
            self.guesses -=1
            letters_guessed.append(letter)

            guessed = self.guessedLetters(secret_word, letters_guessed)

            print('Oops! That letter is not in my word: ',  guessed)
        print('------------')

        return guessed

    def isWordGuessed(self, secret_word, letters_guessed):
        secretLetters = []

        for letter in secret_word:
            if letter in letters_guessed:
                pass
            else:
                return False

        return True

    def guessedLetters(self, secret_word, letters_guessed):

        guessed = self.getGuessedWord()

        for letter in secret_word:
            if letter in letters_guessed:
                guessed += letter
            else:
                guessed += '_ '

        return guessed

    def countDifferentLetters(self, word):
        auxiliar_word = []

        for letter in word:
            if letter not in auxiliar_word:
                auxiliar_word.append(letter)
        different_letters = len(auxiliar_word)

        return different_letters

    def getGuessedWord(self):

         guessed = ''


         return guessed

    def getAvailableLetters(self):
        # 'abcdefghijklmnopqrstuvwxyz'
        available = string.ascii_lowercase

        return available
