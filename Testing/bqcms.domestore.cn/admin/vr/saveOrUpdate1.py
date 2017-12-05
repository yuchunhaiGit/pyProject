__author__ = 'yuchunhai'
#coding=utf-8
#接口说明：冰趣2.2增加的vr页
import requests
url = "http://bqcms.domestore.cn/api/search/vr"
payload = "WzwPhaN96jJDgmK+X7OzJnfHJA8ahp6vfcVOoK6yp8LTQSg3sWEWUA=="
headers = {"Content-Type":"application/json"}
r = requests.post(url,data=payload,headers=headers)
print(r.json())