
def collatz(number):
    if (number % 2) == 0:
        a = number // 2
        return a
    else:
        a = 3 * number + 1
        return a
    
print('Enter a number:')
try:
    while True:
        num = input()
        print(collatz(int(num)))
except ValueError:
    print('Please enter an integer.')
    