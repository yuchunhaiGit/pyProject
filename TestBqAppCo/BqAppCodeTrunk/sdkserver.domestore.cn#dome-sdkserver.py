# coding=utf-8
# @作者:yuchunhai
#@Time:2017/11/29-13:41
#@文件名称:pyProject-sdkserver.domestore.cn#dome-sdkserver
import os
Dir = r'D:\yuchunhaiGit\BqAppCodeTrunk\sdkserver.domestore.cn'
# os.mkdir(Dir)
# os.chdir(Dir)
# os.system(r'svn co http://192.168.7.237/ngsvnroot/dome-sdkserver/trunk')
os.chdir(Dir+'\\trunk')
os.system(r'svn update')
os.system(r'svn info')