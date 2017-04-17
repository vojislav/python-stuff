theBoard = {'a1':'', 'a2':'','a3':'', 'a4':'',
            'b1':'','b2':'','b3':'','b4':'',
            'c1':'','c2':'','c3':'','c4':'',
            'd1':'','d2':'','d3':'','d4':'',}

def printBoard(board):
    print(board['a1'] + ' | ' + board['a2'] + '| ' + board['a3'] + '| ' + board['a4'])
    print('-+-+-+-')
    print(board['b1'] + ' | ' + board['b2'] + '| ' + board['b3'] + '| ' + board['b4'])
    print('-+-+-+-')
    print(board['c1'] + ' | ' + board['c2'] + '| ' + board['c3'] + '| ' + board['c4'])
    print('-+-+-+-')
    print(board['d1'] + ' | ' + board['d2'] + '| ' + board['d3'] + '| ' + board['d4'])
    
turn = 'Player1'
emptyPlaces = 8
print('Place your ships')
 
for i in range(8):
    printBoard(theBoard)
    print('You have ' + str(emptyPlaces) + ' places left.')
    place = input()
    
    if theBoard[place] == '':
        theBoard[place] = 'x'
    
    else:
        print('Place not empty')
        continue
        
    emptyPlaces = emptyPlaces - 1
    
    if emptyPlaces == 0:
        print('You have filled up all empty places')
        printBoard(theBoard)
        
    
    
    
        