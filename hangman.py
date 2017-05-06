import random

words = ['plant', 'human', 'candy', 'dog', 'cat', 'string', 'death', 'coconut']
num = 0
alreadyIndexed = []

print('Welcome to Hangman'.center(30, '-'))
rand = random.randint(0, len(words) - 1)
word = words[rand]
hidWord = '-' * len(word)
print(hidWord)

def checkLetter():
    global hidWord
    letterIndex = word.index(letter)
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
        if str(letter) in word:
            numOfLetter = word.count(letter)
            print(numOfLetter)
            checkLetter()
        else:
            print('Wrong!')