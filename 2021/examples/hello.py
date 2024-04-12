#This program says hello and asks question

print('Hello World!')
print('What is your name?') #ask for name
Name=input()
print('Nice to meet you,' + Name)
print('The length of your name is: ' + str(len(Name)))
print('What is your age?') #ask for age
Age=input()
print('You will be ' + str(int(Age) + 1) + ' in a year')