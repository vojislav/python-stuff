import random

words = [#'plant', 'human', 'candy', 'dog', 'cat', 'string', 'death',
    'coconut']
num = 0

print('Welcome to Hangman'.center(30, '-'))
rand = random.randint(0, len(words) - 1)
word = words[rand]
hidWord = '-' * len(word)
print(hidWord)

for i in range(10):
    if '-' not in hidWord:
        print('Congratz! You got it!')
        quit()
    else:
        print('Guess a letter or the whole word')
        letter = input()
        if str(letter) in word:
            letterIndex = word.index(letter)
            hidWord = list(hidWord)
            hidWord[letterIndex] = letter
            hidWord = "".join(hidWord)
            print(hidWord)
        else:
            print('Wrong!')