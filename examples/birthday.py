birthdays = {'Alice': 'Apr 1', 'Bob': 'Mar 4', 'Tony': 'Apr 28'}

while True:
    print('Enter your friends name: (Blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)

    else:
        print('No birthday found for ' + name)
        print('What is their Birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birhtday database updated.')