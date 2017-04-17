name = ''
while True:
    print('Who are you?')
    name = input()
    
    if name=='Joe':
        print('Hello Joe. Whats the password?')
        password = input()
        
    if password=='swordfish':
            print('Access Granted')
            quit()
    