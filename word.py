import random
import string

WORDLIST_FILENAME = "words.txt"


class Word():

    def __init__(self, guesses):
        self.letters_guessed = []
        self.guesses = guesses

    def loadWords(self):
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
        return random.choice(wordlist)

    def guessLetter(self, letter, secretWord, lettersGuessed, guesses):
        if letter in lettersGuessed:

            guessed = self.guessedLetters(secretWord, lettersGuessed)

            print('Oops! You have already guessed that letter: ', guessed)
        elif letter in secretWord:
            lettersGuessed.append(letter)

            guessed = self.guessedLetters(secretWord, lettersGuessed)

            print('Good Guess: ', guessed)
        else:
            self.guesses -=1
            lettersGuessed.append(letter)

            guessed = self.guessedLetters(secretWord, lettersGuessed)

            print('Oops! That letter is not in my word: ',  guessed)
        print('------------')

        return guessed

    def isWordGuessed(self, secretWord, lettersGuessed):
        secretLetters = []

        for letter in secretWord:
            if letter in lettersGuessed:
                pass
            else:
                return False

        return True

    def guessedLetters(self, secretWord, lettersGuessed):

        guessed = self.getGuessedWord()

        for letter in secretWord:
            if letter in lettersGuessed:
                guessed += letter
            else:
                guessed += '_ '

        return guessed

    def getGuessedWord(self):

         guessed = ''


         return guessed

    def getAvailableLetters(self):
        # 'abcdefghijklmnopqrstuvwxyz'
        available = string.ascii_lowercase

        return available
