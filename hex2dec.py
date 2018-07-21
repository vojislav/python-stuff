import math
letters = ["A", "B", "C", "D", "E", "F"]
numbers = [10, 11, 12, 13, 14, 15]
def dec():
    rems = []
    number = input("enter number (or q to quit):")
    if number == 'q':
        exit()
    while number != 0:
        rem = int(number) % 16
        rems.append(rem)
        number = math.trunc(int(number) / 16)
    rems = rems[::-1]
    for i in rems:
        if(i > 9):
             rems[rems.index(i)] = letters[numbers.index(i)]
    number =''.join(map(str,rems))
    print(number)
    dec()

def hexa():
    list = []
    number1 = 0
    number = input("enter number (or q to quit):")
    number = number.upper()
    if number == 'Q':
        exit()
    for i in str(number):
        list.append(i)
        if i in letters:
            list[list.index(i)] = numbers[letters.index(i)]

    list=list[::-1]
    for i in range(len(list)):
            number1 = number1 + int(list[i]) * 16**i
    print(number1)
    hexa()


def start():
    choice = input(
    '''
    1) Decimal to hexadecimal
    2) Hexadecimal to decimal

    ''')

    if choice == "1":
        dec()
    elif choice == "2":
        hexa()
    else:
        print("Not an option")
        start()
start()
