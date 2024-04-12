#spam = 42 #global variable

def eggs():
    #global spam
    spam = 42 #local variable
    print(spam)

spam = 'Hello'
eggs()
print(spam)