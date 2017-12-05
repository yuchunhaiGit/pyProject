# coding=utf-8
#@作者:yuchunhai
#@Time:2017/11/1413:47
#@文件名称:2c
import os
Dir = 'D:\yuchunhaiGit\pyProject\TestBookGuide\FlaskWeb开发：基于Python的Web应用开发实战.pdf\code'
#创建文件夹
os.mkdir(Dir+r'\2c')
#进入文件夹目录
os.chdir(Dir+r'\2c')
#git命令拉取代码
os.system('git clone https://github.com/miguelgrinberg/flasky.git')
#进入文件夹目录
os.chdir(Dir+r'\2c\flasky')
#git命令拉取代码
os.system('git checkout 2c')