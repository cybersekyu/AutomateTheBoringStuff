import re

def Passcheck(passwd):
    PassRegex = re.compile(r'(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9]).{8,}')
    mo = PassRegex.search(passwd)
    if mo == None:
        print('Sorry, you have a weak password.')
    else:
        print('Your password is strong!')


def PassSlow(passwd):
    PassNum = re.compile(r'[0-9]+')
    PassUpper = re.compile(r'[A-Z]+')
    PassLower = re.compile(r'[a-z]+')
    PassLength = re.compile(r'\w{8,}')

    mo = PassNum.search(passwd)
    mo1 = PassUpper.search(passwd)
    mo2 = PassLower.search(passwd)
    mo3 = PassLength.search(passwd)

    if mo == None:
        print('Password needs to have one number')
    elif mo1 == None:
        print('Password needs to have one uppercase')
    elif mo2 == None:
        print('Password needs to have one lowercase')
    elif mo3 == None:
        print('Password needs to have 8 characters or more')
    else:
        print('Your password is strong!')


PassSlow('Alibata2012')
PassSlow('paosdpaosi')
PassSlow('1234567')
PassSlow('ASDF!@3sasd!')
PassSlow('AAASDSQSQEWEQQWEQE')

