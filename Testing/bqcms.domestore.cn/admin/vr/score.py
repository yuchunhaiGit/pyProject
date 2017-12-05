#coding=utf-8
#@作者:yuchunhai
#@Time:17-11-3下午3:51
#@文件名称:score
import requests
scoreId = 27
while scoreId < 30:
    scoreId = scoreId + 1
    url = "http://bqcms.domestore.cn/admin/vr/score"
    payload = {"id":scoreId,
           "score":"10"
            }
    r = requests.post(url, params=payload)
print(r.json())