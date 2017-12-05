# coding=utf-8
# @作者:yuchunhai
#@Time:2017/11/29-9:28
#@文件名称:pyProject-离线python安装
#容易失败
import os
#暂时没有安装成功的
#selenium-3.7.0安装失败
importToolsRootDir = 'D:\pyTools\Python36\importTools'
importToolsDir = r'\request-0.0.13'
print(importToolsRootDir + importToolsDir)
os.chdir(importToolsRootDir + importToolsDir)
# os.system('python setup.py install')