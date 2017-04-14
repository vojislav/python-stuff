import random

secretNumber = random.randint(1, 5)
print('Im thinking of a number between 1 and 5')

for guessesTaken in range(1, 7):
    print('Make a guess')
    guess = int(input())
    
    if guess > secretNumber:
        print('Too high')
        
    elif guess < secretNumber:
        print('Too low')
        
    else:
        break
    
if guess==secretNumber:
    print('You guessed it in ' + str(guessesTaken)+' tries.')

else:
    print('The number was' + str(secretNumber))