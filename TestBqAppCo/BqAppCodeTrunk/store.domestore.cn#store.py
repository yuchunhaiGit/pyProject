# coding=utf-8
# @作者:yuchunhai
#@Time:2017/11/30-11:49
#@文件名称:pyProject-store.domestore.cn#store
import os
Dir = r'D:\yuchunhaiGit\BqAppCodeTrunk\store(ba).domestore.cn'
# os.mkdir(Dir)
# os.chdir(Dir)
# os.system(r'svn co http://192.168.7.237/ngsvnroot/store/Code-Server/trunk')
os.chdir(Dir+'\\trunk')
os.system(r'svn update')
os.system(r'svn info')