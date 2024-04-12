def collatz(number):
    if (number % 2) == 0:
        num = number // 2
        print(num)
    elif (number % 2) == 1:
        num = 3 * number + 1
        print(num)


print('Hello! please enter a number:')
while True:
    try:    
        innumber = int(input())
        collatz(innumber)
    except ValueError:
        print('Please enter a number not a word/letter')
        continue