__author__ = 'yuchunhai'
#coding=utf-8
#接口说明：冰趣2.2增加的vr页
import requests
url = "http://bqcms.domestore.cn/admin/vr/saveOrUpdate"
payload = {"appCode":"Test-0001217","name":"测试Vr游戏7","devName":"测试开发商","versionCode":"21",
           "introImgs":"https://pic3.zhimg.com/v2-251504fe9be12d630a93ff0c76558caa_r.jpg;https://pic3.zhimg.com/v2-251504fe9be12d630a93ff0c76558caa_r.jpg",
           "intro":"xxx","size":"1500000","status":"1",
           "types":"设计;动作","gameMode":"单人",
            #下面的参数需要真实
           "versionName":"V1.0.1011","pkgName":"com.hunsy.zz","downloadUrl":"http://shouji.360tpcdn.com/170703/cc6d1c761756ada7c73a6d63eb8d653e/net.luoo.FaceFM_15.apk"}
r = requests.post(url, params=payload)
print(r.json())