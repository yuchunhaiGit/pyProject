#coding=utf-8
#@作者:yuchunhai
#@Time:17-11-6下午5:51
#@文件名称:消耗useThings
import requests

url = "http://gamelog.domegame.cn/game/log"

payload = "{\"modelName\":\"useThings\"," \
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
          "\n\"consumeCount\":\"20\"," \
          "\n\"itemId\":\"test001\"," \
          "\n\"itemName\":\"测试物品1\"," \
          "\n\"purpose\":\"1\"," \
          "\n\"curTotal\":\"1124\"\n}"
headers = {
    'modelname': "useThings",
    'appcode': "D00000255",
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "c5a7c5b5-6ca3-3867-e462-ae0c30c65288"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
