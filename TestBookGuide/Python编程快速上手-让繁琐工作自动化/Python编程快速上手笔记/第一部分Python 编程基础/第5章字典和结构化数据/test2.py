'''
Created on 2017年9月21日
 
@author: yuchunhai
'''
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')
        birthdaysNew = {name:bday}
        print(birthdaysNew)
        birthdays.update(birthdaysNew)
        print(birthdays)
