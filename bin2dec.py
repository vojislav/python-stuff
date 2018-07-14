import math
def binary():
    number = input("input number (or q to quit):")
    if number == 'q':
        exit()
    numberDec = 0
    index = 0
    list = []
    for i in number:
        if (i == "0") or (i == "1"):
            list.append(i)
        else:
            print("Not binary")
            binary()

    list = list[::-1]
    for i in list:
        numberDec = numberDec + ((2**index) * int(i))
        index += 1
    print(numberDec)
    binary()

def decimal():
    number = input("input number (or q to quit):")
    if number == 'q':
        exit()
    list = []
    divider = 1
    while (number != 0):
        list.append(int(number)%2)
        number = math.trunc(int(number)/2)
    list = list[::-1]
    numberBin =''.join(map(str,list))
    print(numberBin)
    decimal()

def start():
    print("""
    1) Binary to decimal
    2) Decimal to binary
    """)

    choice = input()

    if choice == "1":
        binary()

    elif choice == "2":
        decimal()

    else:
        print("Not an option")
        start()

start()
