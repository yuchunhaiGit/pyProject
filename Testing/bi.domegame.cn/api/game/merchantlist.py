#coding=utf-8
#@作者:yuchunhai
#@Time:17-11-1下午2:08
#@文件名称:merchantlist
import requests

import login

cookies = login.biCookie()

# cookies = dict(token=login.biCookie())

url = "http://bi.domegame.cn:8008/api/game/merchantlist"
r = requests.get('http://bi.domegame.cn:8008/api/game/merchantlist',cookies = cookies)
print(r.text)