#coding=utf-8
#@作者:yuchunhai
#@Time:17-10-31下午6:01
#@文件名称:getAuthCode
import requests
import json
url = "http://sdkserver.domestore.cn/bqsdklogin/getAuthCode"
payload = {"appCode":"D00000255"
            }
r = requests.post(url, params=payload)
print(r.text)
getAuthCodeBefore = json.loads(r.text)
getAuthCode = getAuthCodeBefore['data']['authCode']
print(getAuthCode)
def authCode():
    return getAuthCode
