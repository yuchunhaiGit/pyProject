# coding=utf-8
# @作者:yuchunhai
#@Time:2017/12/5-17:39
#@文件名称:pyProject-获取轮播列表
#DESUtil文件处理消息解密
import requests
passKey = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCQhIvT60RAT0FJ8tqlV9wN1i8hE37h3IXOxxBwAxkqonFgHw8ucGKT3w8ApGhEgvdRegkHM8/y8MB3l/Q1YOdQMq5DNV5/nHSuYZOTyPE7YlgRj6Xve9KgsRdQT76JIPfCyJd2qCZzsVxsUENZppYPZHAITiOvd8zK9M4cagtkJwIDAQAB'
app = 'bqcms.domestore.cn'
ports = '/api/banner/list'
url = 'http://'+app+ports
r = requests.post(url)
content = r.json()['data']
print(r.json()['data'])
print()

