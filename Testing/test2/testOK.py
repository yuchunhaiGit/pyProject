# coding=utf-8
# @作者:yuchunhai
#@Time:2017/12/8-9:41
#@文件名称:pyProject-testOK
import requests
import json
import Testing.test2.msdnMenu
idGetLangResult = []
urlIndex = "https://msdn.itellyou.cn/Category/Index"
urlGetLang = "https://msdn.itellyou.cn/Category/GetLang"
urlGetList = "https://msdn.itellyou.cn/Category/GetList"
payloadIndex = {
    'id':Testing.test2.msdnMenu.Menu3()
}
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'referer': "https://msdn.itellyou.cn/",
    }
responseIndex = requests.request("POST", urlIndex, data=payloadIndex, headers=headers)

msdnMenu1ListDoing = json.loads(responseIndex.text)
length = len(msdnMenu1ListDoing)

i = 0
while (i < length):
    msdnMenu1ListOK = msdnMenu1ListDoing[i]
    # print(msdnMenu1ListOK['id'])
    idGetLang = msdnMenu1ListOK['id']
    payloadGetLang = {
    'id':idGetLang
    }
    responseGetLang = requests.request("POST", urlGetLang, data=payloadGetLang, headers=headers)
    # print(json.loads(responseGetLang.text))
    # print(json.loads(responseGetLang.text)['result'])
    #返回结果后期优化
    if json.loads(responseGetLang.text)['result'] == idGetLangResult:
        None
        # print('列表数据为空，没有处理的意义')
    else:
        # print(json.loads(responseGetLang.text)['result'][0]['id'])
        print(json.loads(responseGetLang.text)['result'])
    i = i + 1