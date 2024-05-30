allguests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Number of items being brought:')
print('- Apples          ' + str(totalBrought(allguests, 'apples')))
print('- Cups            ' + str(totalBrought(allguests, 'cups')))
print('- Cakes           ' + str(totalBrought(allguests, 'cakes')))
print('- Ham Sandwiches  ' + str(totalBrought(allguests, 'ham sandwiches')))
print('- Apple Pies      ' + str(totalBrought(allguests, 'apple pies')))