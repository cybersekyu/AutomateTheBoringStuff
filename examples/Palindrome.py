number=int(input("Enter any number :"))
"""
reverse_num=0

while(number>0):
    digit=number%10
    reverse_num=reverse_num*10+digit
    number=number//10
"""

numlen=len(str(number))

reverse_num = []

while(numlen > 0):
    reverse_num = str(number)[numlen]
    numlen = numlen - 1 

if(str(number)==str(reverse_num)):
    print('Yes')
    print(reverse_num)
else:
    print('No')
    print(reverse_num)