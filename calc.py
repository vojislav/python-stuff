print('Input first number:')
a = int(input())

if isinstance(a, str) == True:
    print('Not a number')
    exit()
    
print('Input second number:')
b = int(input())

if isinstance(b, str)==True:
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
   
else:
    print('Not an operation')
    quit()