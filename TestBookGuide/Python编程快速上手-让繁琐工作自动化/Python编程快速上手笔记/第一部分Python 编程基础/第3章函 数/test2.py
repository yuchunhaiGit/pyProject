'''
Created on 2017年9月20日
 
@author: yuchunhai
'''

def spam():
    global eggs
    eggs = 43
    print(eggs)
eggs = 44
spam()
print(eggs)