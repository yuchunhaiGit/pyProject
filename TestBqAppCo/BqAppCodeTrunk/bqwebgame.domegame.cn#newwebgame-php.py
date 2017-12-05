# coding=utf-8
# @作者:yuchunhai
#@Time:2017/11/29-13:44
#@文件名称:pyProject-bqwebgame.domegame.cn#newwebgame-php
# 页游平台
#服务端和前端代码地址一致；bqwebgame.domegame.cn/bqstoreba.domegame.cn：
#服务端代码更新即生效；前端代码需要编译；
# /code_dir/gnsrc/newwebgame-php/trunk/webgame
# cnpm run prod

import os
Dir = r'D:\pyTools\BqAppCodeTrunk\bqwebgame(ba).domegame.cn'
# os.mkdir(Dir)
# os.chdir(Dir)
# os.system(r'svn co https://192.168.69.225/svn/newwebgame-php/trunk/webgame')
os.chdir(Dir+'\\webgame')
os.system(r'svn update')
os.system(r'svn info')
