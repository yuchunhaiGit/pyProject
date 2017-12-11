# coding=utf-8
# @作者:yuchunhai
#@Time:2017/12/7-16:19
#@文件名称:pyProject-step3
import requests
import json
url = "https://msdn.itellyou.cn/Category/GetList"
payload = {
    'id':'d15691d5-9208-4a7b-b8f8-b64cf6fb875a',
    'lang':'e15db4de-c094-4c50-822a-98ad50daba4f',
    'filter':'true'
}
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'referer': "https://msdn.itellyou.cn/",
    }
response = requests.request("POST", url, data=payload, headers=headers)
print(json.loads(response.text))
print(json.loads(response.text)['result'][0]['url'])
