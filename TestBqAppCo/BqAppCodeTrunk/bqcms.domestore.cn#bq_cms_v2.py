# coding=utf-8
# @作者:yuchunhai
#@Time:2017/11/29-11:59
#@文件名称:pyProject-bqcms.domestore.cn#bq_cms_v2
import os
Dir = r'D:\yuchunhaiGit\BqAppCodeTrunk\bqcms.domestore.cn'
# os.mkdir(Dir)
# os.chdir(Dir)
# os.system(r'svn co http://192.168.7.237/ngsvnroot/bingqiong/bq_cms_v2/trunk')
os.chdir(Dir+'\\trunk')
os.system(r'svn update')
os.system(r'svn info')