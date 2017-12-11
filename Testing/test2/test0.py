# coding=utf-8
# @作者:yuchunhai
#@Time:2017/12/7-16:26
#@文件名称:pyProject-test0
import requests
import json
url = "https://msdn.itellyou.cn/"
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'referer': "https://msdn.itellyou.cn/",
    }
response = requests.request("GET",url,headers=headers)
print(response.text)