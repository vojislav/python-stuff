abc = 'abcdefghijklmnopqrstuvwxyz'
hor = len(abc)
ver = len(abc)
matrix = [[0 for x in range(hor)] for y in range(ver)]

for i in range(len(abc)):
    abc1 = abc[i:] + abc[:i]
    for j in abc1:
        matrix[abc1.index(j)][i] = j

def printMatrix():
    for i in range(len(abc)):
        print("")
        for j in abc1:
            print(matrix[abc1.index(j)][i], end="")

def encrypt():
    word = input("enter word to encrypt: ")
    key = input("enter key: ")
    key1 = key
    i = 0
    word1 = ""
    while (len(key1) != len(word)):
        if len(word) >= len(key):
            key1 += key[i]
            i += 1
            if i > len(key) - 1:
                i = 0
        else:
            key1 = key1[:-1]

    for i in range(len(word)):
        word1 = word1 + matrix[abc.index(word[i])][abc.index(key1[i])]

    print(word1)

def decrypt():
    word = input("enter word to decrypt: ")
    key = input("enter key: ")
    word1 = ""
    key1 = key
    i = 0
    while (len(key1) != len(word)):
        if len(word) >= len(key):
            key1 += key[i]
            i += 1
            if i > len(key) - 1:
                i = 0
        else:
            key1 = key1[:-1]
    for i in range(len(key1)):
        abc1 = abc[abc.index(key1[i]):] + abc[:abc.index(key1[i])]
        word1 = word1 + matrix[abc1.index(word[i])][0]
    print(word1)

choice = input("""
    1) Encrypt
    2) Decrypt
""")

if choice == "1":
    encrypt()
elif choice == "2":
    decrypt()
else:
    print("Not an option")
    exit()
