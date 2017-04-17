emptyPlaces = 10

for i in range(10):
    print('You have ' + str(emptyPlaces) + ' places left.')
    place = input()
    if place == 'x':
        emptyPlaces = emptyPlaces - 1
        
    else:
        print('Not an option')
        continue
               
    if emptyPlaces == 0:
        print('You have filled up all the empty places')
        break