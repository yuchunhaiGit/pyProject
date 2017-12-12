# coding=utf-8
# @作者:yuchunhai
#@Time:2017/12/12-14:06
#@文件名称:pyProject-msdn.itellyou.cn
import requests
import json
# 企业解决方案
IndexId1 = 'aff8a80f-2dee-4bba-80ec-611ac56d3849'
# MSDN 技术资源库
IndexId2 = '23958de6-bedb-4998-825c-aa3d1e00d097'
# 工具和资源
IndexId3 = '95c4acfd-d1a6-41fe-b14d-a6816973d2aa'
# 应用程序
IndexId4 = '051d75ee-ff53-43fe-80e9-bac5c10fc0fb'
# 开发人员工具
IndexId5 = 'fcf12b78-0662-4dd4-9a82-72040db91c9e'
# 操作系统
IndexId6 = '7ab5f0cb-7607-4bbe-9e88-50716dc43de6'
#服务器
IndexId7 = '36d3766e-0efb-491e-961b-d1a419e06c68'
# 设计人员工具
IndexId8 = '5d6967f0-b58d-4385-8769-b886bfc2b78c'
#请求headers
headers = {
    'content-type':"application/x-www-form-urlencoded",
    'referer': "https://msdn.itellyou.cn/",
    }
#请求接口
urlIndex = "https://msdn.itellyou.cn/Category/Index"
urlGetLang = "https://msdn.itellyou.cn/Category/GetLang"
urlGetList = "https://msdn.itellyou.cn/Category/GetList"
#请求参数处理
# step1:请求Index接口获取二级菜单数据
IndexId = IndexId1
payloadIndex = {
    'id':IndexId
}
responseIndex = json.loads(requests.request("POST", urlIndex, data=payloadIndex, headers=headers).text)
# print(responseIndex)
# step2:使用Index接口返回数据依次请求GetLang接口获取三级菜单数据
i = 0
lengthIndex = len(responseIndex)
while (i < lengthIndex):
    lengthIndexId= responseIndex[i]['id']
    # print(lengthIndexId)
    payloadGetLang = {
    'id':lengthIndexId
    }
    responseGetLang = json.loads(requests.request("POST", urlGetLang, data=payloadGetLang, headers=headers).text)['result']
    # print(responseGetLang)
    #GetLang接口处理，如果为空，不作为GetList接口请求参数
    if responseGetLang == []:
        None
        # print('列表数据为空，没有处理的意义')
    else:
        # print(responseGetLang)
        j = 0
        lengthGetLang = len(responseGetLang)
        while (j < lengthGetLang):
            lengthGetLangId= responseGetLang[j]['id']
            # print(lengthGetLangId)
            payloadGetList = {
                'id':lengthIndexId,
                'lang':lengthGetLangId,
                'filter':'true'
                }
            responseGetList = json.loads(requests.request("POST", urlGetList, data=payloadGetList, headers=headers).text)['result']
            # print(responseGetList)
            if responseGetList == []:
                None
                # print('列表数据为空，没有处理的意义')
            else:
                # print(responseGetList)
                k = 0
                lengthGetList = len(responseGetList)
                while (k < lengthGetList):
                    lengthGetListUrl = responseGetList[k]['url']
                    print(lengthGetListUrl)
                    k = k + 1
            j = j + 1
    i = i + 1