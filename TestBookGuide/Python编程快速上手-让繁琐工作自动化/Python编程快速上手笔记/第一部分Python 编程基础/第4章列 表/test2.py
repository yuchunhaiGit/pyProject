'''
Created on 2017年9月21日
 
@author: yuchunhai
'''
catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +' (Or enter nothing to stop.):')
    name = input()
    if name == '1':
        break
    catNames = catNames + [name] # list concatenation
print('The cat names are:')
for name in catNames:
    print(' ' + name)