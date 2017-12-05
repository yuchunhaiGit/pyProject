#!/usr/bin/python
# Filename: break.py

while True:
    s = input('Enter something(Enter quit to exit):')
    s = s.replace('\r','')
    if s == 'quit':
        break
    print('Length of the string is',len(s))
print('Done')
