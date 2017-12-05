#coding=utf-8
#@作者:yuchunhai
#@Time:17-11-6下午5:45
#@文件名称:消耗物品消耗道具removeitem
import requests

url = "http://gamelog.domegame.cn/game/log"

payload = "{\"modelName\":\"removeitem\"," \
          "\n\"createdAt\":\"2017-11-01 10:11:10\"," \
          "\n\"gameId\":\"D00000255\"," \
          "\n\"gameName\":\"测试游戏1\"," \
          "\n\"version\":\"2\"," \
          "\n\"roleId\":\"3\"," \
          "\n\"serverId\":\"4\"," \
          "\n\"roleName\":\"5\"," \
          "\n\"channelId\":\"6\"," \
          "\n\"roleLv\":\"7\"," \
          "\n\"vipLv\":\"8\"," \
          "\n\"chUserId\":\"9\"," \
          "\n\"bqUserId\":\"49\"," \
          "\n\"typeId\":\"50\"," \
          "\n\"itemId\":\"test001\"," \
          "\n\"itemName\":\"测试物品1\"," \
          "\n\"causeId\":\"1\"," \
          "\n\"quantity\":\"112\"," \
          "\n\"quantityAf\":\"1123\"\n}"
headers = {
    'modelname': "removeitem",
    'appcode': "D00000255",
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "5895151f-8d5d-ff4c-0d19-8d5b3c62a064"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
