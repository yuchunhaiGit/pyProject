#coding=utf-8
#@作者:yuchunhai
#@Time:2017/11/1410:06
#@文件名称:master
import os
Dir = 'D:\yuchunhaiGit\pyProject\TestBookGuide\FlaskWeb开发：基于Python的Web应用开发实战.pdf\code'
#创建文件夹
# os.mkdir(Dir+r'\master')
#进入文件夹目录
os.chdir(Dir+r'\master')
#git命令拉取代码
# os.system('git clone https://github.com/miguelgrinberg/flasky.git')
#git命令更新代码
os.system('git pull')