spam = ['cheetaboo', 'numberblocks', 'blippi']
#spam = []

def commacode(lista):
    for i in range(len(lista)):
        if i != (len(lista) - 1):
            print(lista[i] + ', ', end='')
        else:
            print('and ' + lista[i])

if len(spam) == 0:
    print('There is no item to display')
else:
    commacode(spam)
        