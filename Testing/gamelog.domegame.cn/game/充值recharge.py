#coding=utf-8
#@作者:yuchunhai
#@Time:17-11-6下午5:32
#@文件名称:充值recharge
import requests

url = "http://gamelog.domegame.cn/game/log"

payload = "{\"modelName\":\"recharge\"," \
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
          "\n\"bqUserId\":\"15\"," \
          "\n\"chOrderNo\":\"10\"," \
          "\n\"cpOrderNo\":\"11\"," \
          "\n\"bqOrderNo\":\"12\"," \
          "\n\"rechargeAmount\":\"12\"," \
          "\n\"currency\":\"1\"," \
          "\n\"rechargeType\":\"1\"," \
          "\n\"itemName\":\"测试物品1\"," \
          "\n\"buyedNum\":\"20\"," \
          "\n\"itemId\":\"test001\"," \
          "\n\"valuequantity\":\"21\"," \
          "\n\"deviceNo\":\"899912312301\"," \
          "\n\"ip\":\"192.178.0.1\"," \
          "\n\"valueAmount\":\"25\"\n}"
headers = {
    'modelname': "recharge",
    'appcode': "D00000255",
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "564c7790-070b-7fa6-87bc-1fb8c109b74e"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
