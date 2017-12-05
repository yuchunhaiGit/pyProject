'''
Created on 2017年9月21日
 
@author: yuchunhai
'''
import json
spam = [["1","2","3","4","5","6","7","8"],["A","B","C","D","E"]]
print(spam[0])
print(spam[0][1])
print(spam[1][0:4])
print(len(spam[0]))
spam1 = ["10","11"]
print(spam[0] + spam1)
del spam1[1]
print(spam[0] + spam1)