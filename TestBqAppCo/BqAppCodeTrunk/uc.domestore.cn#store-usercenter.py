# coding=utf-8
# @作者:yuchunhai
#@Time:2017/11/29-13:38
#@文件名称:pyProject-uc.domestore.cn#store-usercenter
import os
Dir = r'D:\yuchunhaiGit\BqAppCodeTrunk\uc.domestore.cn'
# os.mkdir(Dir)
# os.chdir(Dir)
# os.system(r'svn co http://192.168.7.237/ngsvnroot/store-usercenter/trunk')
os.chdir(Dir+'\\trunk')
os.system(r'svn update')
os.system(r'svn info')