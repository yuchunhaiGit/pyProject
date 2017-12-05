# coding=utf-8
# @作者:yuchunhai
#@Time:2017/11/29-10:34
#@文件名称:pyProject-test
import os
con1 = os.system('ipconfig')
con = os.popen('help').read()
file_object = open('D:\pyTools\yutest.txt','w')
file_object.write(con)
file_object1 = open('D:\pyTools\yutest.txt','a')
file_object1.write('1234')
print(con)