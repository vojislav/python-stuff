import random

x = 0
y = 0
tries = 0

rand = random.randint(1, 4)

if rand == 1:
    x = x - 1
    print('x, y('+ str(x) + ', '+ str(y) + ')')
    
elif rand == 2:
    y = y + 1
    print('x, y('+ str(x) + ', '+ str(y) + ')')
    
elif rand == 3:
    x = x + 1
    print('x, y('+ str(x) + ', '+ str(y) + ')')
    
elif rand == 4:
    y = y - 1
    print('x, y('+ str(x) + ', '+ str(y) + ')')

def move():
    global x
    global y
    global tries
    if x == 0 and y ==0:
        print('x, y('+ str(x) + ', '+ str(y) + ')')
        print('It took : ' + str(tries))
        quit()
        
    else:
        rand1 = random.randint(1, 4)
        if rand1 == 1:
            x = x - 1
            print('x, y('+ str(x) + ', '+ str(y) + ')')
            
        elif rand1 == 2:
            y = y + 1
            print('x, y('+ str(x) + ', '+ str(y) + ')')
            
        elif rand1 == 3:
            x = x + 1
            print('x, y('+ str(x) + ', '+ str(y) + ')')
            
        elif rand1 == 4:
            y = y - 1
        tries = tries + 1
        move()
    
move()
