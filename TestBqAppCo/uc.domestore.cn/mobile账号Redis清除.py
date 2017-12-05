# coding=utf-8
# @作者:yuchunhai
#@Time:2017/11/29-14:07
#@文件名称:pyProject-mobile账号Redis清除
import redis
r = redis.StrictRedis(host='192.168.69.229',port=6379,db=0)

mobile = '18601675017'
# mobile = '17373829318'

print(r.hget('uc:basic:mobile:idx',mobile))
print(r.hget('uc:db:idx:mobile',mobile))
r.hdel('uc:basic:mobile:idx',mobile)
r.hdel('uc:db:idx:mobile',mobile)

print('---分割线---')
print(r.hget('uc:basic:mobile:idx',mobile))
print(r.hget('uc:db:idx:mobile',mobile))