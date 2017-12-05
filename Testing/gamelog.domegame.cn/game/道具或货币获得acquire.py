#coding=utf-8
#@作者:yuchunhai
#@Time:17-11-6下午5:25
#@文件名称:道具或货币获得acquire
import requests
url = "http://gamelog.domegame.cn/game/log"
payload = "{\"modelName\":\"acquire\"," \
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
          "\n\"bqUserId\":\"bq001\"," \
          "\n\"obtainTypeId\":\"10\"," \
          "\n\"obtainTypeName\":\"充值\"," \
          "\n\"obtainCount\":\"4\"," \
          "\n\"total\":\"11\"," \
          "\n\"typeId\":\"虚拟币\"," \
          "\n\"itemId\":\"test001\"," \
          "\n\"itemName\":\"测试物品1\"}"
headers = {
    'modelname': "acquire",
    'appcode': "D00000255",
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "3e73e8eb-1e40-8932-5873-f32414fab688"
    }
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)
