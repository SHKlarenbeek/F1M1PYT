import random

words = ["jazz", "abyss", "affix", "Zugzwang", "glowworm", "waltz", "onyx", "jinx", "crypt", "rhythm", "zodiac", "razzmatazz", "kazoo"]



def getrandomword(woordenlijst):
    woordenlijstindex = random.randint(0, len(woordenlijst) -1)
    return woordenlijst[woordenlijstindex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(len(missedLetters))
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)
    
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    while True:
         print('Guess a letter.')
         guess = input()
         guess = guess.lower()
         if len(guess) != 1:
             print('Please enter a single letter.')
         elif guess in alreadyGuessed:
              print('You have already guessed that letter. Choose again.')
         elif guess not in 'abcdefghijklmnopqrstuvwxyz':
             print('Please enter a LETTER.')
         else:
             return guess

def playAgain():
     print('Do you want to play again? (yes or no)')
     return input().lower().startswith('y')

print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getrandomword(words)
gameIsDone = False

while True:
     displayBoard(missedLetters, correctLetters, secretWord)

     guess = getGuess(missedLetters + correctLetters)

     if guess in secretWord:
          correctLetters = correctLetters + guess

          foundAllLetters = True
          for i in range(len(secretWord)):
               if secretWord[i] not in correctLetters:
                    foundAllLetters = False
                    break
          if foundAllLetters:
               print('Yes! The secret word is "' + secretWord + '"! You have won!')
               gameIsDone = True
     else:
         missedLetters = missedLetters + guess

         if len(missedLetters) == 5: 
             displayBoard(missedLetters, correctLetters, secretWord)
             print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
             gameIsDone = True



if gameIsDone:
    if playAgain():
        missedLetters = ''
        correctLetters = ''
        gameIsDone = False
        secretWord = getrandomword(words)
