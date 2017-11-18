import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

Board = {'a0':'_','a1':'_','a2':'_','a3':'_','a4':'_','a5':'_', 'a6':'_','a7':'_', 'a8':'_','a9':'_',
         'b0':'_','b1':'_','b2':'_','b3':'_','b4':'_','b5':'_', 'b6':'_','b7':'_', 'b8':'_','b9':'_',
         'c0':'_','c1':'_','c2':'_','c3':'_','c4':'_','c5':'_', 'c6':'_','c7':'_', 'c8':'_','c9':'_',
         'd0':'_','d1':'_','d2':'_','d3':'_','d4':'_','d5':'_', 'd6':'_','d7':'_', 'd8':'_','d9':'_',
         'e0':'_','e1':'_','e2':'_','e3':'_','e4':'_','e5':'_', 'e6':'_','e7':'_', 'e8':'_','e9':'_',
         'f0':'_','f1':'_','f2':'_','f3':'_','f4':'_','f5':'_', 'f6':'_','f7':'_', 'f8':'_','f9':'_',
         'g0':'_','g1':'_','g2':'_','g3':'_','g4':'_','g5':'_', 'g6':'_','g7':'_', 'g8':'_','g9':'_',
         'h0':'_','h1':'_','h2':'_','h3':'_','h4':'_','h5':'_', 'h6':'_','h7':'_', 'h8':'_','h9':'_',
         'i0':'_','i1':'_','i2':'_','i3':'_','i4':'_','i5':'_', 'i6':'_','i7':'_', 'i8':'_','i9':'_',
         'j0':'_','j1':'_','j2':'_','j3':'_','j4':'_','j5':'_', 'j6':'_','j7':'_', 'j8':'_','j9':'_'}

enemyBoard={'a0':'_','a1':'_','a2':'_','a3':'_','a4':'_','a5':'_', 'a6':'_','a7':'_', 'a8':'_','a9':'_',
            'b0':'_','b1':'_','b2':'_','b3':'_','b4':'_','b5':'_', 'b6':'_','b7':'_', 'b8':'_','b9':'_',
            'c0':'_','c1':'_','c2':'_','c3':'_','c4':'_','c5':'_', 'c6':'_','c7':'_', 'c8':'_','c9':'_',
            'd0':'_','d1':'_','d2':'_','d3':'_','d4':'_','d5':'_', 'd6':'_','d7':'_', 'd8':'_','d9':'_',
            'e0':'_','e1':'_','e2':'_','e3':'_','e4':'_','e5':'_', 'e6':'_','e7':'_', 'e8':'_','e9':'_',
            'f0':'_','f1':'_','f2':'_','f3':'_','f4':'_','f5':'_', 'f6':'_','f7':'_', 'f8':'_','f9':'_',
            'g0':'_','g1':'_','g2':'_','g3':'_','g4':'_','g5':'_', 'g6':'_','g7':'_', 'g8':'_','g9':'_',
            'h0':'_','h1':'_','h2':'_','h3':'_','h4':'_','h5':'_', 'h6':'_','h7':'_', 'h8':'_','h9':'_',
            'i0':'_','i1':'_','i2':'_','i3':'_','i4':'_','i5':'_', 'i6':'_','i7':'_', 'i8':'_','i9':'_',
            'j0':'_','j1':'_','j2':'_','j3':'_','j4':'_','j5':'_', 'j6':'_','j7':'_', 'j8':'_','j9':'_'}

usedPlayerPlaces = []
usedEnemyPlaces = []

places =   ['a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9',
            'b0', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9',
            'c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9',
            'd0', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9',
            'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9',
            'f0', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
            'g0', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'g9',
            'h0', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9',
            'i0', 'i1', 'i2', 'i3', 'i4', 'i5', 'i6', 'i7', 'i8', 'i9',
            'j0', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'j8', 'j9']

enemyPlaces =  ['a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9',
                'b0', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9',
                'c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9',
                'd0', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9',
                'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9',
                'f0', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
                'g0', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'g9',
                'h0', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9',
                'i0', 'i1', 'i2', 'i3', 'i4', 'i5', 'i6', 'i7', 'i8', 'i9',
                'j0', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'j8', 'j9']

def printBoard(board):
    print('  0 1 2 3 4 5 6 7 8 9')
    
    print('A'+ ' ' + board['a0'] + ' ' + board['a1'] + ' ' + board['a2'] + ' ' + board['a3'] + ' ' + board['a4'] + ' ' + board['a5'] + ' ' + board['a6'] + ' ' + board['a7'] + ' ' + board['a8']  + ' ' + board['a9'])
    
    print('B'+ ' ' + board['b0'] + ' ' + board['b1'] + ' ' + board['b2'] + ' ' + board['b3'] + ' ' + board['b4'] + ' ' + board['b5'] + ' ' + board['b6'] + ' ' + board['b7'] + ' ' + board['b8']  + ' ' + board['b9'])

    print('C'+ ' ' + board['c0'] + ' ' + board['c1'] + ' ' + board['c2'] + ' ' + board['c3'] + ' ' + board['c4'] + ' ' + board['c5'] + ' ' + board['c6'] + ' ' + board['c7'] + ' ' + board['c8']  + ' ' + board['c9'])

    print('D'+ ' ' + board['d0'] + ' ' + board['d1'] + ' ' + board['d2'] + ' ' + board['d3'] + ' ' + board['d4'] + ' ' + board['d5'] + ' ' + board['d6'] + ' ' + board['d7'] + ' ' + board['d8']  + ' ' + board['d9'])

    print('E'+ ' ' + board['e0'] + ' ' + board['e1'] + ' ' + board['e2'] + ' ' + board['e3'] + ' ' + board['e4'] + ' ' + board['e5'] + ' ' + board['e6'] + ' ' + board['e7'] + ' ' + board['e8']  + ' ' + board['e9'])

    print('F'+ ' ' + board['f0'] + ' ' + board['f1'] + ' ' + board['f2'] + ' ' + board['f3'] + ' ' + board['f4'] + ' ' + board['f5'] + ' ' + board['f6'] + ' ' + board['f7'] + ' ' + board['f8']  + ' ' + board['f9'])

    print('G'+ ' ' + board['g0'] + ' ' + board['g1'] + ' ' + board['g2'] + ' ' + board['g3'] + ' ' + board['g4'] + ' ' + board['g5'] + ' ' + board['g6'] + ' ' + board['g7'] + ' ' + board['g8']  + ' ' + board['g9'])

    print('H'+ ' ' + board['h0'] + ' ' + board['h1'] + ' ' + board['h2'] + ' ' + board['h3'] + ' ' + board['h4'] + ' ' + board['h5'] + ' ' + board['h6'] + ' ' + board['h7'] + ' ' + board['h8']  + ' ' + board['h9'])

    print('I'+ ' ' + board['i0'] + ' ' + board['i1'] + ' ' + board['i2'] + ' ' + board['i3'] + ' ' + board['i4'] + ' ' + board['i5'] + ' ' + board['i6'] + ' ' + board['i7'] + ' ' + board['i8']  + ' ' + board['i9'])

    print('J'+ ' ' + board['j0'] + ' ' + board['j1'] + ' ' + board['j2'] + ' ' + board['j3'] + ' ' + board['j4'] + ' ' + board['j5'] + ' ' + board['j6'] + ' ' + board['j7'] + ' ' + board['j8']  + ' ' + board['j9'])
    print('\n')
print('-----BATTLESHIP-----')
input("Press ENTER to start the game.")
clear()
print('Place your ships')
print('\n')

turn = 0
prevDir = ''

def start(): 
    playerShip(5)
    clear() 
    playerShip(4) 
    clear() 
    playerShip(3)
    clear() 
    playerShip(3)
    clear() 
    playerShip(2)
    clear() 
    printBoard(Board)
    input('Press ENTER to continue')
    clear()

def playerShip(length):
    global Board
    ships = ['Submarine', 'Cruiser']
    random.shuffle(ships)
    printBoard(Board)
    if length == 2:
        shipType = 'Destroyer'
    elif length == 3:
        shipType = ships[0]
    elif length == 3:
        shipType = ships[1]
    elif length == 4:
        shipType = 'Battleship'
    elif length == 5:
        shipType = 'Carrier'
    print('Ship type : ' + shipType)
    print('Ship length : ' + str(length))
    print('Pick starting position:')
    place = input()
    alphabet = 'abcdefghij'
    letterIndex = alphabet.index(place[0])
    if len(place) < 3:
        print('Pick direction(r, l, u or d)')
        dir = input()
        if dir == 'r':
            endPlace = place[0] + str((int(place[1]) + length))
            if (place in Board) and (endPlace in Board) and (Board[endPlace] == '_') and (Board[place] == '_'):
                for i in range(length):
                    if Board[place[0] + str(int(place[1]) + i)] == '_':
                        Board[place[0] + str(int(place[1]) + i)] = 'o'
                        usedPlayerPlaces.append(place[0] + str(int(place[1]) + i))
                    else:
                        print('NOT OK2')
                        Board = dict.fromkeys(Board, '_')
                        start()
                
            else:
                print('NOT OK1')
                Board = dict.fromkeys(Board, '_')
                start()


        elif dir == 'l':
            endPlace = place[0] + str((int(place[1]) - length))
            if (place in Board) and (endPlace in Board) and (Board[endPlace] == '_') and (Board[place] == '_'):
                for i in range(length):
                    if Board[place[0] + str(int(place[1]) - i)] == '_':
                        Board[place[0] + str(int(place[1]) - i)] = 'o'
                        usedPlayerPlaces.append(place[0] + str(int(place[1]) - i))
                    else:
                        print('NOT OK2')
                        Board = dict.fromkeys(Board, '_')
                        start()
                
            else:
                print('NOT OK1')
                Board = dict.fromkeys(Board, '_')
                start()
    
        elif dir == 'u':
            if (place in Board) and (Board[place] == '_'):
                for i in range(length):
                    secLetterIndex = letterIndex - i
                    if secLetterIndex >= 0:
                        if Board[alphabet[secLetterIndex] + place[1]] == '_':
                            Board[alphabet[secLetterIndex] + place[1]] = 'o'
                            usedPlayerPlaces.append(alphabet[secLetterIndex] + place[1])
                        else:
                            print('NOT OK2')
                            Board = dict.fromkeys(Board, '_')
                            start()
                    else:
                        Board = dict.fromkeys(Board, '_')
                        start()

            else:
                print('NOT OK1')
                start()
    
        elif dir == 'd':
            if (place in Board) and (Board[place] == '_'):
                for i in range(length):
                    secLetterIndex = letterIndex + i
                    if secLetterIndex <= 9:
                        if Board[alphabet[secLetterIndex] + place[1]] == '_':
                            Board[alphabet[secLetterIndex] + place[1]] = 'o'
                            usedPlayerPlaces.append(alphabet[secLetterIndex] + place[1])
                        else:
                            print('NOT OK2')
                            Board = dict.fromkeys(Board, '_')
                            start()
                    else:
                        Board = dict.fromkeys(Board, '_')
                        start()
            else:
                print('NOT OK1')
                Board = dict.fromkeys(Board, '_')
                start()

def enemyBoardMaker(length): 
    global enemyBoard
    global enemyPlaces
    global usedEnemyPlaces
    alphabet = 'abcdefghij'
    possibleDirs = []
    place = random.choice(enemyPlaces)
    letterIndex = alphabet.index(place[0])

    if int(place[1]) <= 9 - length + 1:
        for i in range(length):
            if enemyBoard[place[0] + str(int(place[1]) + i)] == '_':
                if 'r' not in possibleDirs:
                    possibleDirs.append('r')
        
                if letterIndex >=  length - 1:
                    secLetterIndex = letterIndex - i
                    if enemyBoard[alphabet[secLetterIndex] + place[1]] == '_':
                        if 'u' not in possibleDirs:
                            possibleDirs.append('u')
                    
                if letterIndex <= 9 - length + 1:
                    secLetterIndex = letterIndex + i
                    if enemyBoard[alphabet[secLetterIndex] + place[1]] == '_':
                        if 'd' not in possibleDirs:
                            possibleDirs.append('d')
            
    if int(place[1]) >= length - 1:
        for i in range(length):
                if enemyBoard[place[0] + str(int(place[1]) - i)] == '_':
                    if 'l' not in possibleDirs:
                        possibleDirs.append('l')
                
                if letterIndex >=  length - 1:
                    secLetterIndex = letterIndex - i
                    if enemyBoard[alphabet[secLetterIndex] + place[1]] == '_':
                        if 'u' not in possibleDirs:
                            possibleDirs.append('u')
                        
                if letterIndex <= 9 - length + 1:
                    secLetterIndex = letterIndex + i
                    if enemyBoard[alphabet[secLetterIndex] + place[1]] == '_':
                        if 'd' not in possibleDirs:
                            possibleDirs.append('d')
                            
    direc = random.choice(possibleDirs)
    
    if direc == 'r':
        for i in range(length):
            if int(place[1]) + i <= 9:            
                if enemyBoard[place[0] + str(int(place[1]) + i)] == '_':
                    enemyBoard[place[0] + str(int(place[1]) + i)] = 'o'
                    if place[0] + str(int(place[1]) + i) in enemyPlaces:
                        enemyPlaces.remove(place[0] + str(int(place[1]) + i))
                        if place[0] + str(int(place[1]) + i) not in usedEnemyPlaces:
                            usedEnemyPlaces.append(place[0] + str(int(place[1]) + i))
                else:
                   enemyBoard = dict.fromkeys(enemyBoard, '_')
                   break
            else:
                enemyBoard = dict.fromkeys(enemyBoard, '_')
                break
                
    elif direc == 'l':
        for i in range(length):
            if int(place[1]) - i >= 0:
                if enemyBoard[place[0] + str(int(place[1]) - i)] == '_':
                    enemyBoard[place[0] + str(int(place[1]) - i)] = 'o'
                    if place[0] + str(int(place[1]) - i) in enemyPlaces:
                        enemyPlaces.remove(place[0] + str(int(place[1]) - i))
                        if place[0] + str(int(place[1]) - i) not in usedEnemyPlaces:
                            usedEnemyPlaces.append(place[0] + str(int(place[1]) - i))
                else:
                   enemyBoard = dict.fromkeys(enemyBoard, '_')
                   break
            else:
                enemyBoard = dict.fromkeys(enemyBoard, '_')
                break
                
    elif direc == 'u':
        for i in range(length):
            secLetterIndex = letterIndex - i
            if secLetterIndex >= 0:
                if enemyBoard[alphabet[secLetterIndex] + place[1]] == '_':
                    enemyBoard[alphabet[secLetterIndex] + place[1]] = 'o'
                    if alphabet[secLetterIndex] + place[1] in enemyPlaces:
                        enemyPlaces.remove(alphabet[secLetterIndex] + place[1])
                        if alphabet[secLetterIndex] + place[1] not in usedEnemyPlaces:
                            usedEnemyPlaces.append(alphabet[secLetterIndex] + place[1])
                else:
                    enemyBoard = dict.fromkeys(enemyBoard, '_')
                    break
            else:
                enemyBoard = dict.fromkeys(enemyBoard, '_')
                break
                
    elif direc == 'd':
        for i in range(length):
            secLetterIndex = letterIndex + i
            if secLetterIndex <= 9:
                if enemyBoard[alphabet[secLetterIndex] + place[1]] == '_':
                    enemyBoard[alphabet[secLetterIndex] + place[1]] = 'o'
                    if alphabet[secLetterIndex] + place[1] in enemyPlaces:
                        enemyPlaces.remove(alphabet[secLetterIndex] + place[1])
                        if alphabet[secLetterIndex] + place[1] not in usedEnemyPlaces:
                            usedEnemyPlaces.append(alphabet[secLetterIndex] + place[1])
                else:
                    enemyBoard = dict.fromkeys(enemyBoard, '_')
                    break
            else:
                enemyBoard = dict.fromkeys(enemyBoard, '_')
                break
            
    enemyPlaces = ['a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9',
                'b0', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9',
                'c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9',
                'd0', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9',
                'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9',
                'f0', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
                'g0', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'g9',
                'h0', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9',
                'i0', 'i1', 'i2', 'i3', 'i4', 'i5', 'i6', 'i7', 'i8', 'i9',
                'j0', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'j8', 'j9']

def enemyBoardDrawer():
    global enemyPlaces
    global enemyBoard
    global usedEnemyPlaces
    
    while len(usedEnemyPlaces) != 17:
        enemyBoard = dict.fromkeys(enemyBoard, '_')
        usedEnemyPlaces = []
        enemyPlaces =  ['a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9',
                        'b0', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9',
                        'c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9',
                        'd0', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9',
                        'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9',
                        'f0', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
                        'g0', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'g9',
                        'h0', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9',
                        'i0', 'i1', 'i2', 'i3', 'i4', 'i5', 'i6', 'i7', 'i8', 'i9',
                        'j0', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'j8', 'j9']
        
        enemyBoardMaker(5)
        enemyBoardMaker(4)
        enemyBoardMaker(3)
        enemyBoardMaker(3)
        enemyBoardMaker(2)
        
    enemyBoard = dict.fromkeys(enemyBoard, '_')
    print('ENEMY BOARD READY!')
    print('------------------------------')
    input('Press ENTER to continue')
    clear()

def playerTurn():
    global turn
    while turn == 0:
        print('-----ENEMY BOARD-----')
        printBoard(enemyBoard)
        print('Guess a position:')
        playerGuess = input()
        if len(playerGuess) == 0:
            clear()
            print('THATS NOT A POSITION...ITS NOT ANYTHING ACTUALLY')
            playerTurn()
        clear()
        if playerGuess in enemyPlaces:
            if playerGuess in usedEnemyPlaces:
                print('HIT!')
                enemyBoard[playerGuess] = ('0')
                usedEnemyPlaces.remove(playerGuess)
                enemyPlaces.remove(playerGuess)
                printBoard(enemyBoard)
                input('Press ENTER to continue')
                clear()
                
            else:
                print('MISS!')
                enemyBoard[playerGuess] = ('x')
                enemyPlaces.remove(playerGuess)
                printBoard(enemyBoard)
                turn = 1
                input('Press ENTER to continue')
                clear()
                
        else:
            clear()
            print('YOU ALREDY GUESSED THAT POSITION')
            playerTurn()
            
        if len(usedEnemyPlaces) == 0:
            print('YOU WON!')
            input('Press ENTER to quit')
            quit() 

def enemyTurn():
    global turn
    global printBoard
    global prevDir
    while turn == 1:
        print('-----PLAYER BOARD-----')
        printBoard(Board)
        input('Press ENTER to continue')
        clear()
        enemyGuess = random.choice(places)
        if enemyGuess in usedPlayerPlaces:
            print('YOU\'VE BEEN HIT!')
            Board[enemyGuess] = ('0')
            usedPlayerPlaces.remove(enemyGuess)
            places.remove(enemyGuess)
            printBoard(Board)
            input('Press ENTER to continue')
            clear()
            while turn == 1:
                alphabet = 'abcdefghij'
                letterIndex = alphabet.index(enemyGuess[0])
                dirs = ['u', 'r', 'd', 'l']
                if prevDir == '':
                    randDir = random.choice(dirs)
                if randDir == 'u':
                    prevDir = 'u'
                    secLetterIndex = letterIndex - 1
                    secEnemyGuess = alphabet[secLetterIndex] + enemyGuess[1]
                    if secEnemyGuess in usedPlayerPlaces:
                        print('YOU\'VE BEEN HIT!')
                        Board[secEnemyGuess] = ('0')
                        usedPlayerPlaces.remove(secEnemyGuess)
                        places.remove(secEnemyGuess)
                        printBoard(Board)
                        turn = 1
                        enemyGuess = secEnemyGuess
                        input('Press ENTER to continue')
                        clear()
                    
                    
                    elif secEnemyGuess in places:
                        print('THE ENEMY MISSED!')
                        Board[secEnemyGuess] = ('x')
                        places.remove(secEnemyGuess)
                        printBoard(Board)
                        turn = 0
                        prevDir = ''
                        input('Press ENTER to continue')
                        clear()
                        break
                        
                    else:
                        turn = 0
                        prevDir = ''
                        break
                        
                        
                elif randDir == 'd':
                    prevDir = 'd'
                    secLetterIndex = letterIndex + 1
                    secEnemyGuess = alphabet[secLetterIndex] + enemyGuess[1]
                    if secEnemyGuess in usedPlayerPlaces:
                        print('YOU\'VE BEEN HIT!')
                        Board[secEnemyGuess] = ('0')
                        usedPlayerPlaces.remove(secEnemyGuess)
                        places.remove(secEnemyGuess)
                        printBoard(Board)
                        turn = 1
                        enemyGuess = secEnemyGuess
                        input('Press ENTER to continue')
                        clear()
                        
                    
                    elif secEnemyGuess in places:
                        print('THE ENEMY MISSED!')
                        Board[secEnemyGuess] = ('x')
                        places.remove(secEnemyGuess)
                        printBoard(Board)
                        turn = 0
                        prevDir = ''
                        input('Press ENTER to continue')
                        clear()
                        break
                        
                    else:
                        turn = 0
                        prevDir = ''
                        break
                        
                    
                elif randDir == 'r':
                    prevDir = 'r'
                    secEnemyGuess = enemyGuess[0] + str(int(enemyGuess[1]) + 1)
                    if secEnemyGuess in usedPlayerPlaces:
                        print('YOU\'VE BEEN HIT!')
                        Board[secEnemyGuess] = ('0')
                        usedPlayerPlaces.remove(secEnemyGuess)
                        places.remove(secEnemyGuess)
                        printBoard(Board)
                        turn = 1
                        enemyGuess = secEnemyGuess
                        input('Press ENTER to continue')
                        clear()
                        
                    
                    elif secEnemyGuess in places:
                        print('THE ENEMY MISSED!')
                        Board[secEnemyGuess] = ('x')
                        places.remove(secEnemyGuess)
                        printBoard(Board)
                        turn = 0
                        prevDir = ''
                        input('Press ENTER to continue')
                        clear()
                        break
                        
                    
                    else:
                        turn = 0
                        prevDir = ''
                        break
                        
                        
                elif randDir == 'l':
                    prevDir = 'l'
                    secEnemyGuess = enemyGuess[0] + str(int(enemyGuess[1]) - 1)
                    if secEnemyGuess in usedPlayerPlaces:
                        print('YOU\'VE BEEN HIT!')
                        Board[secEnemyGuess] = ('0')
                        usedPlayerPlaces.remove(secEnemyGuess)
                        places.remove(secEnemyGuess)
                        printBoard(Board)
                        turn = 1
                        enemyGuess = secEnemyGuess
                        input('Press ENTER to continue')
                        clear()
                       
                    
                    elif secEnemyGuess in places:
                        print('THE ENEMY MISSED!')
                        Board[secEnemyGuess] = ('x')
                        places.remove(secEnemyGuess)
                        printBoard(Board)
                        turn = 0
                        prevDir = ''
                        input('Press ENTER to continue')
                        clear()
                        break
                    
                    else:
                        turn = 0
                        prevDir = ''
                        break
        else:
            print('THE ENEMY MISSED!')
            Board[enemyGuess] = ('x')
            places.remove(enemyGuess)
            printBoard(Board)
            turn = 0
            input('Press ENTER to continue')
            clear()
            break
    
        if len(usedPlayerPlaces) == 0:
            print('THE ENEMY WON!')
            input('Press ENTER to quit')
            quit() 
start()
enemyBoardDrawer()
while len(usedPlayerPlaces) > 0 or len(usedEnemyPlaces) > 0:
    playerTurn()
    enemyTurn()
