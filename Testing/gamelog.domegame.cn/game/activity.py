#coding=utf-8
#@作者:yuchunhai
#@Time:17-11-6下午5:28
#@文件名称:活动activity
import sys
import requests

url = "http://gamelog.domegame.cn/game/log"

payload = "{\"modelName\":\"activity\"," \
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
          "\n\"bqUserId\":\"11\"," \
          "\n\"activityId\":\"10\"," \
          "\n\"itemId\":\"test001\"," \
          "\n\"itemName\":\"测试物品1\"," \
          "\n\"obtainCount\":\"6\"\n}"
headers = {
    'modelname': "activity",
    'appcode': "D00000255",
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "b8a59757-8794-66db-873e-901e7a4fd5d2"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
