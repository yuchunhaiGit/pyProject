'''
Created on 2017年9月21日
 
@author: yuchunhai
'''
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
print(birthdays.get('Alice',123))
print(birthdays.get('yu1'))
print(birthdays.get('yu',123))