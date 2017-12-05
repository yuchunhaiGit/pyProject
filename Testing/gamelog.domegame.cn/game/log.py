#coding=utf-8
#@作者:yuchunhai
#@Time:17-11-6下午2:57
#@文件名称:log
import requests
import json

url = "http://gamelog.domegame.cn/game/log"
header = {"modelName": "acquire", "appCode": "V-0002", "Content-Type": "application/json;charset=utf-8"}
payload = {"modelName": "acquire",
           "createdAt": "2017-11-01 10:11:10",
           "gameId": "YY-0002",
           "gameName": "测试游戏1",
           "version": "2",
           "roleId": "3",
           "serverId": "4",
           "roleName": "5",
           "channelId": "6",
           "roleLv": "7",
           "vipLv": "8",
           "chUserId": "9",
           "bqUserId": "bq001",
           "obtainTypeId": "10",
           "obtainTypeName": "充值",
           "obtainCount": "4",
           "total": "11",
           "typeId": "虚拟币",
           "itemId": "test001",
           "itemName": "测试物品1"}
r = requests.post(url, params=payload, headers=header, json=json)
print(r.json())