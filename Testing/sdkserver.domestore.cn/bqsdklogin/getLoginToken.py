#coding=utf-8
#@作者:yuchunhai
#@Time:17-10-31下午6:02
#@文件名称:getLoginToken
import requests
url = "http://sdkserver.domestore.cn/bqsdklogin/getLoginToken"
payload = {"countryCode":"",
           "password":'8CE33881717D365B8EBEF25510D89457',
           "passport":"17700090007",
           "clientId":"D00000218",
           "buId":"DOME001",
           "sysType":"AD",
           "channelId":"CHA000002"
            }
r = requests.post(url, params=payload)
print(r.text)