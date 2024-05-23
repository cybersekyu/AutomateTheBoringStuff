import random

numstreaks = 0
for experimentnum in range(10000):
    #Code that creates a list of 100 heads or tails values
    coinlist = []
    for i in range(100):
        if random.randint(0, 1) == 1:
            coinlist.append('H')
        else:
            coinlist.append('T')
    #Code that checks if there is a streak of 6 heads or tails in a row.
    for i in range(len(coinlist)):
        count = 0
        for x in range(6):
            try:
                if coinlist[i] == coinlist[i + x]:
                    count += 1
                else:
                    break
            except IndexError:
                break
        if count == 6:
            numstreaks += 1

print(numstreaks)    
print('Chance of Streak: %s%%' % (numstreaks / 100))