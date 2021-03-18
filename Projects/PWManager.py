#! python3
# PWManager.py - A simple and insecure password manager. Can also become a copy and paste program

# TODO: enhance this to be useful drafting email responses.

PASSWORDS = {'email': 'ASDA!@#DASDASDASDADASDAS',
             'blog': 'AASDFDFWEFSCVSerwewrfdSD',
             'luggage': '12345'}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python PWManager.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first command line argument is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no password saved for account named' + account)

#@py.exe C:\Python34\PWManager.py %*    ------ To create a bat file for windows
#@pause