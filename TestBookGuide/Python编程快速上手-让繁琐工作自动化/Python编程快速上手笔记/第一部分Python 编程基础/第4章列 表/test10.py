'''
Created on 2017年9月21日
 
@author: yuchunhai
'''
import copy
yu = ['A','B','C','D','E','F','G']
yu1 = copy.copy(yu)
yu1[1] = 42
print(yu)
print(yu1)