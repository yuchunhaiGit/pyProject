# coding=utf-8
# @作者:yuchunhai
#@Time:2017/11/29-11:47
#@文件名称:pyProject-文件处理
# 1、os.path.exists(path) 判断一个目录是否存在
# 2、os.makedirs(path) 多层创建目录
# 3、os.mkdir(path) 创建目录
# 在以上DEMO的函数里，我并没有使用os.mkdir(path)函数，而是使用了多层创建目录函数os.makedirs(path)。这两个函数之间最大的
# 区别是当父目录不存在的时候os.mkdir(path)不会创建，os.makedirs(path)则会创建父目录
