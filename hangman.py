import random

words = ['plant', 'human', 'candy', 'dog', 'cat', 'string', 'death']
num = 0

'Welcome to Hangman'.center(20, '-')
rand = random.randint(0, len(words) - 1)
word = words[rand]
hidWord = '_' * len(word)
print(hidWord)

for i in range(len(word)):
    print('Guess a letter or the whole word')
    letter = input()
    if len(letter) == 1:
        if i == letter:
            hidWord[i] = word[i]
            num += 1
        else:
            print('Wrong')
            continue