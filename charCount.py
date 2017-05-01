import pprint

print('Enter text:')
message = input()
count={}

for char in message:
    count.setdefault(char, 0)
    count[char] = count[char] + 1
    
pprint.pprint(count)
