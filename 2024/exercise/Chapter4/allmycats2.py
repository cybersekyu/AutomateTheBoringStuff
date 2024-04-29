cats = []
while True:
    print('Enter the name of the cat ' + str(len(cats) + 1) + ' or enter nothing to stop.')
    name = input()
    if name == '':
        break
    cats = cats + [name]
print('The cat names are: ')
for name in cats:
    print(' ' + name)    