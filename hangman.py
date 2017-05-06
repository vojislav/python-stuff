import random
import re

words = ['plant', 'human', 'candy', 'dog', 'cat', 'string', 'death', 'coconut']

print('Welcome to Hangman'.center(30, '-'))
rand = random.randint(0, len(words) - 1)
word = words[rand]
hidWord = '-' * len(word)
print(hidWord)

def checkLetter(letterIndex):
    global hidWord
    #letterIndex = word.index(letter)
    hidWord = list(hidWord)
    hidWord[letterIndex] = letter
    hidWord = "".join(hidWord)
    print(hidWord)

for i in range(10):
    if '-' not in hidWord:
        print('Congratz! You got it!')
        quit()
    else:
        print('Guess a letter or the whole word')
        letter = input()
        charIndexes = ([m.start() for m in re.finditer(letter, word)])
        if str(letter) in word:
            for i in charIndexes:
                checkLetter(i)
        else:
            print('Wrong!')