import random
theBoard = {'a0':'_','a1':'_','a2':'_','a3':'_','a4':'_','a5':'_', 'a6':'_','a7':'_', 'a8':'_','a9':'_',
            'b0':'_','b1':'_','b2':'_','b3':'_','b4':'_','b5':'_', 'b6':'_','b7':'_', 'b8':'_','b9':'_',
            'c0':'_','c1':'_','c2':'_','c3':'_','c4':'_','c5':'_', 'c6':'_','c7':'_', 'c8':'_','c9':'_',
            'd0':'_','d1':'_','d2':'_','d3':'_','d4':'_','d5':'_', 'd6':'_','d7':'_', 'd8':'_','d9':'_',
            'e0':'_','e1':'_','e2':'_','e3':'_','e4':'_','e5':'_', 'e6':'_','e7':'_', 'e8':'_','e9':'_',
            'f0':'_','f1':'_','f2':'_','f3':'_','f4':'_','f5':'_', 'f6':'_','f7':'_', 'f8':'_','f9':'_',
            'g0':'_','g1':'_','g2':'_','g3':'_','g4':'_','g5':'_', 'g6':'_','g7':'_', 'g8':'_','g9':'_',
            'h0':'_','h1':'_','h2':'_','h3':'_','h4':'_','h5':'_', 'h6':'_','h7':'_', 'h8':'_','h9':'_',
            'i0':'_','i1':'_','i2':'_','i3':'_','i4':'_','i5':'_', 'i6':'_','i7':'_', 'i8':'_','i9':'_',
            'j0':'_','j1':'_','j2':'_','j3':'_','j4':'_','j5':'_', 'j6':'_','j7':'_', 'j8':'_','j9':'_'}
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
    print('')
turn = 'Player1'
emptyPlaces = 8
print('Place your ships')

def ship(length):
    global theBoard
    ships = ['Submarine', 'Cruiser']
    random.shuffle(ships)
    
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
    if len(place) < 3:
        print('Pick direction(R, L, U or D)')
        dir = input()
        if dir == 'r':
            endPlace = place[0] + str((int(place[1]) + length))
            if (place in theBoard) and (endPlace in theBoard) and (theBoard[endPlace] == '_') and (theBoard[place] == '_'):
                for i in range(length):
                    if theBoard[place[0] + str(int(place[1]) + i)] == '_':
                        theBoard[place[0] + str(int(place[1]) + i)] = 'o'
                    else:
                        print('NOT OK2')
                        theBoard = dict.fromkeys(theBoard, '_')
                printBoard(theBoard)
                
            else:
                print('NOT OK1')
    
        elif dir == 'l':
            endPlace = place[0] + str((int(place[1]) - length))
            if (place in theBoard) and (endPlace in theBoard) and (theBoard[endPlace] == '_') and (theBoard[place] == '_'):
                for i in range(length):
                    if theBoard[place[0] + str(int(place[1]) - i)] == '_':
                        theBoard[place[0] + str(int(place[1]) - i)] = 'o'
                    else:
                        print('NOT OK2')
                        theBoard = dict.fromkeys(theBoard, '_')
                printBoard(theBoard)
                
            else:
                print('NOT OK1')
    
        elif dir == 'u':
            if (place in theBoard) and (theBoard[place] == '_'):
                for i in range(length):
                    if place[0] == 'a':
                        letterPos = 0
                        
                    if place[0] == 'b':
                        letterPos = 1
                        
                    if place[0] == 'c':
                        letterPos = 2
                        
                    if place[0] == 'd':
                        letterPos = 3
                        
                    if place[0] == 'e':
                        letterPos = 4
                        
                    if place[0] == 'f':
                        letterPos = 5
                        
                    if place[0] == 'g':
                        letterPos = 6
                        
                    if place[0] == 'h':
                        letterPos = 7
                        
                    if place[0] == 'i':
                        letterPos = 8
                        
                    if place[0] == 'j':
                        letterPos = 9
                        
                    if letterPos < length - 1: #or (letterPos > (9 - length) + 1):
                        print('NOT OK 2')
                        quit()
                        
                    endLetterPos = letterPos - i
                    
                    if endLetterPos == 0:
                        endLetter = 'a'
                        
                    if endLetterPos == 1:
                        endLetter = 'b'
                        
                    if endLetterPos == 2:
                        endLetter = 'c'
                        
                    if endLetterPos == 3:
                        endLetter = 'd'
                        
                    if endLetterPos == 4:
                        endLetter = 'e'
                        
                    if endLetterPos == 5:
                        endLetter = 'f'
                        
                    if endLetterPos == 6:
                        endLetter = 'g'
                        
                    if endLetterPos == 7:
                        endLetter = 'h'
                        
                    if endLetterPos == 8:
                        endLetter = 'i'
                        
                    if endLetterPos == 9:
                        endLetter = 'j'
                        
                    if theBoard[endLetter + place[1]] == '_':
                        theBoard[endLetter + place[1]] = 'o'
                    else:
                        print('NOT OK3')
                        theBoard = dict.fromkeys(theBoard, '_')
                printBoard(theBoard)

            else:
                print('NOT OK1')
    
        elif dir == 'd':
            if (place in theBoard) and (theBoard[place] == '_'):
                for i in range(length):
                    if place[0] == 'a':
                        letterPos = 0
                        
                    if place[0] == 'b':
                        letterPos = 1
                        
                    if place[0] == 'c':
                        letterPos = 2
                        
                    if place[0] == 'd':
                        letterPos = 3
                        
                    if place[0] == 'e':
                        letterPos = 4
                        
                    if place[0] == 'f':
                        letterPos = 5
                        
                    if place[0] == 'g':
                        letterPos = 6
                        
                    if place[0] == 'h':
                        letterPos = 7
                        
                    if place[0] == 'i':
                        letterPos = 8
                        
                    if place[0] == 'j':
                        letterPos = 9
                        
                    if (letterPos > (9 - length) + 1):
                        print('NOT OK 2')
                        quit()
                        
                    endLetterPos = letterPos + i
                    
                    if endLetterPos == 0:
                        endLetter = 'a'
                        
                    if endLetterPos == 1:
                        endLetter = 'b'
                        
                    if endLetterPos == 2:
                        endLetter = 'c'
                        
                    if endLetterPos == 3:
                        endLetter = 'd'
                        
                    if endLetterPos == 4:
                        endLetter = 'e'
                        
                    if endLetterPos == 5:
                        endLetter = 'f'
                        
                    if endLetterPos == 6:
                        endLetter = 'g'
                        
                    if endLetterPos == 7:
                        endLetter = 'h'
                        
                    if endLetterPos == 8:
                        endLetter = 'i'
                        
                    if endLetterPos == 9:
                        endLetter = 'j'

                    if theBoard[endLetter - place[1]] == '_':
                        theBoard[endLetter - place[1]] = 'o'
                    else:
                        print('NOT OK3')
                        theBoard = dict.fromkeys(theBoard, '_')
                printBoard(theBoard)

            else:
                print('NOT OK1')
    
ship(2)