spam = ['apples', 'bananas', 'tofu', 'cats', 'dogs', 'human', 'toys']

def commacode(listss):
    for i in range(len(listss)):
        if i != (len(listss) - 1):
            print(listss[i] + ', ', end='')
        else:
            print('and ' + listss[i])

commacode(spam)