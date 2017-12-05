#coding=utf-8
#@作者:yuchunhai
#@Time:17-11-1下午2:16
#@文件名称:login
import requests
payload = dict(name='admin', password='123123')
print(payload)
url = "http://bi.domegame.cn:8008/api/admin/login"
r = requests.post(url,data=payload)
print(r.text)
print('url地址',r.url)
print('编码',r.encoding)
print('状态码',r.status_code)
headers = r.headers['Set-Cookie']
print('headers',r.headers['Set-Cookie'])
print('返回文本',r.text)
print('json',r.json())
print('原始数据',r.raw)
print('错误请求信息',r.raise_for_status())
print('cookies',r.cookies)
print('history',r.history)
def biCookie():
    return headers