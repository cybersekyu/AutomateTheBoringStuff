'''
name = 'Bob'

if name == 'Alice':
    print('Hi Alice')
print('done')

password = 'swordfish1'
if password == 'swordfish':
    print('Access Granted')
else:
    print('Wrong Password')

name = 'Bob'
age = 3000
if name == 'Alice':
    print('Hi Alice')
elif age < 12:
    print('You are not Alice, Kiddo.')
elif age > 2000:
    print('Are you a vampire?')
elif age > 100:
    print('Grandma is that you?')  

''' 

print('Enter your name:')

name = input()

if name:
    print('Thank you for entering your name')
else:
    print('You did not enter a name')