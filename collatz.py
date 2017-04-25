print('Enter a number:')
number = int(input())

while number != 1:
    if number == 1:
        break

    if number%2 == 0:
        number = number//2
        print(str(number))

    elif number%2 == 1:
        number = 3*number+1
        print(str(number))
