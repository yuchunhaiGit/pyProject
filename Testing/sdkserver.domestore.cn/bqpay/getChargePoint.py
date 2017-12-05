#coding=utf-8
#@作者:yuchunhai
#@Time:17-10-31下午5:43
#@文件名称:getChargePoint
import requests
url = "http://sdkserver.domestore.cn/bqpay/getChargePoint"
payload = {"appCode":"D00000255",
           "chargePointCode":"C00000812",
           "channelCode":"D00000255",
           "authToken":"RDAwMDAwMjE4|YnFfMDAwMjMwMDI2|1509441954114|9c66d7dc8ff3df978628fbb3d3bdcf5f",
           }
r = requests.post(url, params=payload)
print(r.text)
