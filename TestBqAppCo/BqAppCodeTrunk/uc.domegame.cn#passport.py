# coding=utf-8
# @作者:yuchunhai
#@Time:2017/11/29-13:34
#@文件名称:pyProject-uc.domegame.cn#passport
import os
Dir = r'D:\yuchunhaiGit\BqAppCodeTrunk\uc.domegame.cn'
# os.mkdir(Dir)
# os.chdir(Dir)
# os.system(r'svn co http://192.168.7.237/ngsvnroot/front/bingqiong/trunk/web/passport')
os.chdir(Dir+'\\passport')
os.system(r'svn update')
os.system(r'svn info')