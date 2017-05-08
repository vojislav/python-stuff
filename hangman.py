import random # for finding a random word
import re # for finding all instances of a letter

words = ['plant', 'human', 'candy', 'dog', 'cat', 'string', 'death', 'coconut',
    'vacuum cleaner', 'ice cream'] # words to choose from

print('Welcome to Hangman'.center(30, '-'))

def start():
    global hidWord
    global word
    global turns
    
    turns = 0
    rand = random.randint(0, len(words) - 1) # random num for words list index
    word = words[rand] 
    if ' ' in word: # checking the word has a space (if it's a two-part word)
        space = word.index(' ') # finding the index of the space in the word
        firstPart = word[:space] # first half, from the beginning to the space
        secondPart = word[space:] # second half, from the space to the end
        hidWord = '-' * len(firstPart) + ' ' + '-' * (len(secondPart) - 1) # defining hidWord again as the firstPart in dashes and the secondPart in dashes
                                                                           #(for some reason it kept adding another dash at the end of the secondPart, hence the - 1)
    else:
        hidWord = '-' * len(word) # if not a two-part word
    
def game():
    global letter
    
    print(hidWord)
    print(str(turns) + ' Guess a letter or the whole word (/quit - to quit)')
    letter = input()
    charIndexes = ([m.start() for m in re.finditer(letter, word)]) # I legit dunno how this works 
                                                                   #(looks for indexes of all instances of letter in word and places them in list charIndexes)
    if letter == word: # checking if whole word guessed
         print('Congratz! You got it!')
         again()
    elif letter in word: # if letter in word
        for i in charIndexes: # loops for each i in charIndexes
            checkLetter(i) # checkLetter func with parameter i (takes i, an index of a character, and uses it in place of letterIndex in function)
        #print(hidWord)
        
    elif letter == ':':
        print('Wrong!')
        
    elif letter == '/quit':
        quit()
        
    else:
        print('Wrong!') # if wrong
        
def checkLetter(letterIndex): # defining func to check if letter is in word, with parameter letterIndex
    global hidWord
    hidWord = list(hidWord)
    hidWord[letterIndex] = letter
    hidWord = "".join(hidWord)

def again():
    print('Try again?(y/n)')
    answer = input()
    if answer == 'y':
        start()
    else:
        quit()

start()

while turns <= 10: # loops 10 times
    if '-' not in hidWord: # checking if done
        print('Congratz! You got it!')
        again()
    else:
        game()
    
    turns += 1

print(word) # if not guessed within 10 turns, prints out word
again()