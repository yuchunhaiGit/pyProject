'''
Created on 2017年9月20日
 
@author: yuchunhai
'''

while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == '111111':
        break
print('Access granted.')