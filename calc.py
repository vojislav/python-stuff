print('Input first number:')
a = input()

if isinstance(int(a), str) == True:
    print('Not a number')
    exit()
    
print('Input second number:')
b = input()

if isinstance(int(b), str)==True:
        print('Not a number')
        exit()
        
print('Select operation(+,-,*,/, ^)')
c = input()

if c == '+':
    z=int(a)+int(b)
    print(z)
    quit()
    
elif c == '-':
    z=int(a)-int(b)
    print(z)
    quit()
    
elif c == '*':
    z=int(a)*int(b)
    print(z)
    quit()
    
elif c == '/':
    z=int(a)/int(b)
    print(z)
    quit()
    
elif c == '^':
    z=int(a)**int(b)
    print(z)
    quit()
   
if c != '+, -, *, /, ^':
    print('Not an operation')
    quit()