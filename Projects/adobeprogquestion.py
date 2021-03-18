# TODO: create a function that will remove duplicate numbers in lists and index itself.

def unique():
    number = [222, 333, 333, 222, 555]
    for i in range(len(number)):
        #x = number[i]
        d = 0
        for nextarray in range(i):
         if number[i] == number[nextarray]:
            d = 1
            break
        if (d == 0):
            print(number[i] , end=' ')

unique()



#def checkserver():