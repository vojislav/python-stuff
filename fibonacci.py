a = 1
b = 1
print(str(a))
print(str(b))

for i in range(150):
   c = a + b
   print(str(c))
   a = b
   b = c
