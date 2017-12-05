'''
Created on 2017年9月20日
 
@author: yuchunhai
'''
import sys
while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')