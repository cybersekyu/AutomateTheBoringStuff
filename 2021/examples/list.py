dogName = []

while True:
    print('Enter the name of the dog ' + str(len(dogName) + 1)  + ' (Or enter nothing to stop.): ') #str just adds number to state the number of the dog
    name = input()
    if name == '':
        break
    dogName = dogName + [name] #list concatenation

print('The dog names are:')

for name in dogName:
    print(' ' + name)