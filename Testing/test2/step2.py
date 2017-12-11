# coding=utf-8
# @作者:yuchunhai
#@Time:2017/12/7-16:18
#@文件名称:pyProject-step2
import requests
import json
import Testing.test2.step1
url = "https://msdn.itellyou.cn/Category/GetLang"
# payload = "id=d15691d5-9208-4a7b-b8f8-b64cf6fb875a"
payload = {
    'id':Testing.test2.step1.Menu1ListOK()
}
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'referer': "https://msdn.itellyou.cn/",
    }
response = requests.request("POST", url, data=payload, headers=headers)
print(json.loads(response.text))
